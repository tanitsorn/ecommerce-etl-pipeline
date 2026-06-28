1. Dataset Overview
    - customers: 99,441 rows, 5 columns
    - orders: order transaction table
    - order_items: line item level (fact table)
    - products: product dimension
2. Data Structure
    - customers → primary key: customer_id
    - orders → primary key: order_id, foreign key: customer_id
    - order_items → order_id + product_id
3. Missing Values Analysis
    - orders: missing values in delivery timestamps (depends on order status)
    - products: very few missing rows (~2)
    - customers: no missing values
4. Data Quality Issues
    - Order lifecycle not complete for all records
    - Cancelled / unavailable orders should be excluded from revenue
    - Product names are missing (only length fields exist)
5. Relationship Mapping
    customers → orders → order_items → products