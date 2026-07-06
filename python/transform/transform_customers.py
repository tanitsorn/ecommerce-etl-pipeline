from python.extract.extract_data import load_customers
from python.utils.file_utils import save_csv

def transform_customers():
    # Load data
    customers = load_customers()

    # Remove duplicates
    customers = customers.drop_duplicates()

    # Standardize city
    customers["customer_city"] = (
        customers["customer_city"]
        .str.strip()
        .str.lower()
    )
    # Standardize state
    customers["customer_state"] = (
        customers["customer_state"]
        .str.strip()
        .str.upper()
    )

    # Save cleaned dataset
    save_csv(customers, "customers.csv")
    
    return customers

if __name__ == "__main__":
    transform_customers()