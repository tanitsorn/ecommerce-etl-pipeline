import pandas as pd
from unittest.mock import MagicMock, patch

from python.load.load_to_mysql import load_to_mysql


def test_load_to_mysql():
    mock_engine = MagicMock()

    mock_customers = pd.DataFrame({
        "customer_id": ["C1"],
        "customer_unique_id": ["U1"],
        "customer_zip_code_prefix": [12345],
        "customer_city": ["sao paulo"],
        "customer_state": ["SP"],
    })

    mock_products = pd.DataFrame({
        "product_id": ["P1"],
        "product_category_name": ["electronics"],
    })

    mock_orders = pd.DataFrame({
        "order_id": ["O1"],
        "order_status": ["delivered"],
        "order_purchase_timestamp": [pd.Timestamp("2017-10-02")],
        "order_approved_at": [pd.Timestamp("2017-10-02")],
        "order_delivered_carrier_date": [pd.Timestamp("2017-10-04")],
        "order_delivered_customer_date": [pd.Timestamp("2017-10-10")],
        "order_estimated_delivery_date": [pd.Timestamp("2017-10-18")],
    })

    mock_order_items = pd.DataFrame({
        "order_id": ["O1"],
        "order_item_id": [1],
        "product_id": ["P1"],
        "seller_id": ["S1"],
        "shipping_limit_date": [pd.Timestamp("2017-10-05")],
        "price": [29.99],
        "freight_value": [5.00],
    })

    mock_csv_data = [
        mock_customers,
        mock_products,
        mock_orders,
        mock_order_items,
    ]

    with patch(
        "python.load.load_to_mysql.get_engine",
        return_value=mock_engine
    ), patch(
        "python.load.load_to_mysql.pd.read_csv",
        side_effect=mock_csv_data
    ) as mock_read_csv, patch(
        "pandas.DataFrame.to_sql"
    ) as mock_to_sql:

        load_to_mysql()

    assert mock_read_csv.call_count == 4
    assert mock_to_sql.call_count == 4

    table_names = [
        call.args[0]
        for call in mock_to_sql.call_args_list
    ]

    assert table_names == [
        "customers",
        "products",
        "orders",
        "order_items",
    ]

    mock_engine.dispose.assert_called_once()