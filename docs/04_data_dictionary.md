# Data Dictionary

## Project
E-commerce Analytics ETL Pipeline


# 1. Customers

| Column | Description | Data Type | Used For | Transform |
|---------|-------------|-----------|----------|-----------|
| customer_id | Unique identifier for each customer record. | String | Join with orders table | No |
| customer_unique_id | Unique identifier representing the same customer across multiple purchases. | String | Repeat customer analysis | No |
| customer_zip_code_prefix | Customer ZIP code prefix. | Integer | Future geographic analysis | No |
| customer_city | Customer city. | String | Future geographic analysis | Standardize text if necessary |
| customer_state | Customer state abbreviation. | String | Future geographic analysis | Standardize text if necessary |


# 2. Orders

| Column | Description | Data Type | Used For | Transform |
|---------|-------------|-----------|----------|-----------|
| order_id | Unique order identifier. | String | Join with order_items table | No |
| customer_id | Customer foreign key. | String | Join with customers table | No |
| order_status | Current order status. | String | Filter valid business transactions | Filter delivered orders for analytics |
| order_purchase_timestamp | Purchase datetime. | Datetime | Sales trend analysis | Convert to datetime |
| order_approved_at | Order approval datetime. | Datetime | Future process analysis | Convert to datetime |
| order_delivered_carrier_date | Carrier pickup datetime. | Datetime | Future logistics analysis | Convert to datetime |
| order_delivered_customer_date | Customer delivery datetime. | Datetime | Delivery performance analysis | Convert to datetime |
| order_estimated_delivery_date | Estimated delivery datetime. | Datetime | Delivery performance analysis | Convert to datetime |

Derived Columns

- delivery_days = order_delivered_customer_date - order_purchase_timestamp


# 3. Order Items

| Column | Description | Data Type | Used For | Transform |
|---------|-------------|-----------|-----------|
| order_id | Order foreign key. | String | Join with orders table | No |
| order_item_id | Item sequence within an order. | Integer | Identify each item within an order | No |
| product_id | Product foreign key. | String | Join with products table |  No |
| seller_id | Seller identifier. | String | Future seller performance analysis | No |
| shipping_limit_date | Shipping deadline. | Datetime | Future logistics analysis | Convert to datetime |
| price | Product selling price. | Float | Revenue calculation | No |
| freight_value | Shipping fee charged for the item. | Float | Revenue calculation | No |

Derived Columns

- revenue = price + freight_value
    - Used for sales and revenue analytics


# 4. Products

| Column | Description | Data Type | Used For | Transform |
|---------|-------------|-----------|----------|-----------|
| product_id | Unique product identifier. | String | Join with order_items table | No |
| product_category_name | Product category. | String | Product category analysis | Handle missing values |
| product_name_length | Length of product name. | Float | Future product metadata analysis | Handle missing values |
| product_description_length | Length of product description. | Float | Future product metadata analysis | Handle missing values |
| product_photos_qty | Number of product photos. | Float | Future product metadata analysis | Handle missing values |
| product_weight_g | Product weight (grams). | Float | Future logistics analysis | Validate datatype |
| product_length_cm | Product length (cm). | Float | Future logistics analysis | Validate datatype |
| product_height_cm | Product height (cm). | Float | Future logistics analysis | Validate datatype |
| product_width_cm | Product width (cm). | Float | Future logistics analysis | Validate datatype |