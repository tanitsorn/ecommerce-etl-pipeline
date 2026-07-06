import pandas as pd
from sqlalchemy import create_engine, text
from python.utils.config import MYSQL_CONFIG


def get_engine():
    return create_engine(
        f"mysql+pymysql://{MYSQL_CONFIG['user']}:{MYSQL_CONFIG['password']}"
        f"@{MYSQL_CONFIG['host']}:{MYSQL_CONFIG['port']}/{MYSQL_CONFIG['database']}"
    )


def load_to_mysql():

    engine = get_engine()

    # Clear old data
    with engine.begin() as conn:
        conn.execute(text("SET FOREIGN_KEY_CHECKS = 0"))

        conn.execute(text("TRUNCATE TABLE order_items"))
        conn.execute(text("TRUNCATE TABLE orders"))
        conn.execute(text("TRUNCATE TABLE products"))
        conn.execute(text("TRUNCATE TABLE customers"))

    # Load customers
    customers = pd.read_csv("data/clean/customers.csv")
    customers.to_sql(
        "customers",
        engine,
        if_exists="append",
        index=False,
    )
    print(f"✓ Loaded customers ({len(customers):,} rows)")

    # Load products
    products = pd.read_csv("data/clean/products.csv")
    products.to_sql(
        "products",
        engine,
        if_exists="append",
        index=False,
    )
    print(f"✓ Loaded products ({len(products):,} rows)")

    # Load orders
    orders = pd.read_csv(
        "data/clean/orders.csv",
        parse_dates=[
            "order_purchase_timestamp",
            "order_approved_at",
            "order_delivered_carrier_date",
            "order_delivered_customer_date",
            "order_estimated_delivery_date",
        ],
    )
    orders.to_sql(
        "orders",
        engine,
        if_exists="append",
        index=False,
    )
    print(f"✓ Loaded orders ({len(orders):,} rows)")

    # Load order items
    order_items = pd.read_csv(
        "data/clean/order_items.csv",
        parse_dates=["shipping_limit_date"],
    )
    order_items.to_sql(
        "order_items",
        engine,
        if_exists="append",
        index=False,
    )
    print(f"✓ Loaded order_items ({len(order_items):,} rows)")

    # Enable foreign key checks again
    with engine.begin() as conn:
        conn.execute(text("SET FOREIGN_KEY_CHECKS = 1"))

    engine.dispose()

    print("✓ All tables loaded successfully!")


if __name__ == "__main__":
    load_to_mysql()