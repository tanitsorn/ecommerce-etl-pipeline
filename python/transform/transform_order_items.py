import pandas as pd
from python.extract.extract_data import load_order_items
from python.utils.file_utils import save_csv

def transform_order_items():
    # Load data
    order_items = load_order_items()

    # Remove duplicates
    order_items = order_items.drop_duplicates()

    # Convert datetime
    order_items["shipping_limit_date"] = pd.to_datetime(
        order_items["shipping_limit_date"]
    )

    # Save cleaned data
    save_csv(order_items, "order_items.csv")

    return order_items

if __name__ == "__main__":
    transform_order_items()