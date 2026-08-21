import pandas as pd

from python.extract.extract_data import (
    extract_all,
    load_customers,
    load_orders,
    load_order_items,
    load_products,
)


def test_load_customers():
    df = load_customers()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty


def test_load_orders():
    df = load_orders()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty


def test_load_order_items():
    df = load_order_items()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty


def test_load_products():
    df = load_products()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty


def test_extract_all():
    customers, orders, order_items, products = extract_all()

    assert isinstance(customers, pd.DataFrame)
    assert isinstance(orders, pd.DataFrame)
    assert isinstance(order_items, pd.DataFrame)
    assert isinstance(products, pd.DataFrame)

    assert not customers.empty
    assert not orders.empty
    assert not order_items.empty
    assert not products.empty

def test_customers_schema():
    df = load_customers()

    expected_columns = {
        "customer_id",
        "customer_unique_id",
        "customer_zip_code_prefix",
        "customer_city",
        "customer_state",
    }

    assert expected_columns.issubset(df.columns)