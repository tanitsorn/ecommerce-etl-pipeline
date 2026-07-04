from python.extract.extract_data import load_products
from python.utils.file_utils import save_csv

def transform_products():
    # Load data
    products = load_products()

    # Remove duplicates
    products = products.drop_duplicates()

    # Fill missing category
    products["product_category_name"] = (
        products["product_category_name"]
        .fillna("unknown")
        .str.strip()
        .str.lower()
    )

    # Fill missing numeric values
    numeric_columns = [
        "product_name_lenght",
        "product_description_lenght",
        "product_photos_qty",
        "product_weight_g",
        "product_length_cm",
        "product_height_cm",
        "product_width_cm",
    ]

    for col in numeric_columns:
        products[col] = products[col].fillna(0)

    # Save cleaned data
    save_csv(products, "products.csv")

    return products

if __name__ == "__main__":
    transform_products()