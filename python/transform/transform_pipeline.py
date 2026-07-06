from python.transform.transform_customers import transform_customers
from python.transform.transform_orders import transform_orders
from python.transform.transform_order_items import transform_order_items
from python.transform.transform_products import transform_products

def run_transform_pipeline():
    print("Starting data transformation...")

    transform_customers()
    print("✓ Customers transformed")

    transform_orders()
    print("✓ Orders transformed")

    transform_order_items()
    print("✓ Order Items transformed")

    transform_products()
    print("✓ Products transformed")

    print("Data transformation completed!")

if __name__ == "__main__":
    run_transform_pipeline()