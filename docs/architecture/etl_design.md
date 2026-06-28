1. ETL Overview
    This project implements an ETL pipeline for e-commerce sales analytics.
    The pipeline extracts raw CSV data, transforms it using Python (Pandas), and loads cleaned data into MySQL for analytics and reporting.

2. Data Flow Diagram
    Customers (raw CSV)
        ↓
    Orders (raw CSV)
            ↓
    Order Items (raw CSV)
            ↓
    Products (raw CSV)
            ↓
    Python ETL (Extract → Transform → Load)
            ↓
    MySQL Database
            ↓
    SQL Analytics Layer
            ↓
    Business Insights (Revenue, Delivery Time, etc.)

3. Business Logic (Revenue, Delivery Time)
    Revenue = price + freight_value
    Delivery Time = order_delivered_date - order_purchase_date
    Include only orders with status = delivered for analytics
    Exclude canceled / unavailable orders from revenue calculation

4. Transformation Rules
    - Handle missing values in orders (especially timestamps)
    - Convert all date columns to datetime format
    - Remove invalid or incomplete orders for analytics
    - Normalize product category text
    - Compute revenue per order item
    - Compute delivery time per order

5. Load Strategy
    - Load transformed data into MySQL tables
    - Use batch insert for performance
    - Separate tables for:
        - cleaned_orders
        - order_items_fact
        - product_dimension
        - customer_dimension

        