import pandas as pd
from unittest.mock import patch

from python.transform.transform_customers import transform_customers
from python.transform.transform_orders import transform_orders
from python.transform.transform_order_items import transform_order_items
from python.transform.transform_products import transform_products


def test_transform_customers():
    mock_data = pd.DataFrame({
        "customer_id": ["1", "2", "2"],
        "customer_unique_id": ["A", "B", "B"],
        "customer_zip_code_prefix": [12345, 23456, 23456],
        "customer_city": ["  sao paulo ", "RIO DE JANEIRO", "RIO DE JANEIRO"],
        "customer_state": ["sp", "rj", "rj"],
    })

    with patch(
        "python.transform.transform_customers.load_customers",
        return_value=mock_data
    ), patch(
        "python.transform.transform_customers.save_csv"
    ):
        result = transform_customers()

    assert isinstance(result, pd.DataFrame)

    assert len(result) == 2

    assert result["customer_city"].tolist() == [
        "sao paulo",
        "rio de janeiro"
    ]

    assert result["customer_state"].tolist() == [
        "SP",
        "RJ"
    ]


def test_transform_orders():
    mock_data = pd.DataFrame({
        "order_id": ["1", "2", "2"],
        "order_status": ["delivered", "shipped", "shipped"],
        "order_purchase_timestamp": [
            "2017-10-02 10:56:33",
            "2018-07-24 20:41:37",
            "2018-07-24 20:41:37",
        ],
        "order_approved_at": [
            "2017-10-02 11:07:15",
            "2018-07-24 20:55:09",
            "2018-07-24 20:55:09",
        ],
        "order_delivered_carrier_date": [
            "2017-10-04 19:55:00",
            "2018-07-26 14:31:00",
            "2018-07-26 14:31:00",
        ],
        "order_delivered_customer_date": [
            "2017-10-10 21:25:13",
            "2018-08-02 15:07:00",
            "2018-08-02 15:07:00",
        ],
        "order_estimated_delivery_date": [
            "2017-10-18",
            "2018-08-13",
            "2018-08-13",
        ],
    })

    with patch(
        "python.transform.transform_orders.load_orders",
        return_value=mock_data
    ), patch(
        "python.transform.transform_orders.save_csv"
    ):
        result = transform_orders()

    assert isinstance(result, pd.DataFrame)

    # Check duplicates were removed
    assert len(result) == 2

    # Check datetime columns were converted
    datetime_columns = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date",
    ]

    for col in datetime_columns:
        assert pd.api.types.is_datetime64_any_dtype(result[col])


def test_transform_order_items():
    mock_data = pd.DataFrame({
        "order_id": ["1", "2", "2"],
        "order_item_id": [1, 1, 1],
        "product_id": ["A", "B", "B"],
        "seller_id": ["S1", "S2", "S2"],
        "shipping_limit_date": [
            "2017-09-19 09:45:35",
            "2017-09-20 10:30:00",
            "2017-09-20 10:30:00",
        ],
        "price": [29.99, 49.99, 49.99],
        "freight_value": [5.00, 10.00, 10.00],
    })

    with patch(
        "python.transform.transform_order_items.load_order_items",
        return_value=mock_data
    ), patch(
        "python.transform.transform_order_items.save_csv"
    ):
        result = transform_order_items()

    assert isinstance(result, pd.DataFrame)

    # Check duplicates were removed
    assert len(result) == 2

    # Check shipping_limit_date was converted to datetime
    assert pd.api.types.is_datetime64_any_dtype(
        result["shipping_limit_date"]
    )


def test_transform_products():
    mock_data = pd.DataFrame({
        "product_id": ["P1", "P2", "P2"],
        "product_category_name": ["  electronics ", None, None],
        "product_name_lenght": [10, None, None],
        "product_description_lenght": [100, None, None],
        "product_photos_qty": [3, None, None],
        "product_weight_g": [500, None, None],
        "product_length_cm": [20, None, None],
        "product_height_cm": [10, None, None],
        "product_width_cm": [15, None, None],
    })

    with patch(
        "python.transform.transform_products.load_products",
        return_value=mock_data
    ), patch(
        "python.transform.transform_products.save_csv"
    ):
        result = transform_products()

    assert isinstance(result, pd.DataFrame)

    # Check duplicates were removed
    assert len(result) == 2

    # Check category cleaning
    assert result["product_category_name"].tolist() == [
        "electronics",
        "unknown"
    ]

    # Check missing numeric values were filled with 0
    numeric_columns = [
        "product_name_length",
        "product_description_length",
        "product_photos_qty",
        "product_weight_g",
        "product_length_cm",
        "product_height_cm",
        "product_width_cm",
    ]

    for col in numeric_columns:
        assert result[col].isna().sum() == 0

    # Check column names were corrected
    assert "product_name_length" in result.columns
    assert "product_description_length" in result.columns

    assert "product_name_lenght" not in result.columns
    assert "product_description_lenght" not in result.columns