import pandas as pd
from python.extract.extract_data import load_orders
from python.utils.file_utils import save_csv

def transform_orders():
    # Load data
    orders = load_orders()

    # Remove duplicates
    orders = orders.drop_duplicates()

    # Convert datetime columns
    datetime_columns = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date",
    ]

    for col in datetime_columns:
        orders[col] = pd.to_datetime(orders[col])

    # Save cleaned dataset
    save_csv(orders, "orders.csv")

    return orders

if __name__ == "__main__":
    transform_orders()