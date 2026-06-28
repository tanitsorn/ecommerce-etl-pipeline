import pandas as pd
def load_customers():
    return pd.read_csv("data/raw/olist_customers_dataset.csv")

def load_orders():
    return pd.read_csv("data/raw/olist_orders_dataset.csv")

def load_order_items():
    return pd.read_csv("data/raw/olist_order_items_dataset.csv")

def load_products():
    return pd.read_csv("data/raw/olist_products_dataset.csv")

def extract_all():
    customers = load_customers()
    orders = load_orders()
    order_items = load_order_items()
    products = load_products()
    return customers, orders, order_items, products