# E-commerce ETL Pipeline

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.x-green)
![MySQL](https://img.shields.io/badge/MySQL-8-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

## Overview

An end-to-end ETL project built with Python, SQL, and MySQL using the Brazilian E-Commerce Public Dataset by Olist.

This project demonstrates practical Data Engineering skills including data extraction, transformation, loading, relational database design, and business analytics.

---

## Objectives

* Build a production-style ETL pipeline.
* Transform raw e-commerce data into analytics-ready datasets.
* Load transformed data into MySQL.
* Answer business questions using SQL.

---

## Dataset

This project uses the Brazilian E-commerce Public Dataset by Olist.

**Source:**
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

Tables used:

- Customers
- Orders
- Order Items
- Products

Raw files are stored in:

```text
data/raw/
```

Transformed datasets are stored in:

```text
data/clean/
```
---

## Technology Stack

* Python
* Pandas
* SQLAlchemy
* PyMySQL
* MySQL
* SQL
* Git
* GitHub
* Visual Studio Code

---

## Architecture

```text
                +----------------------+
                |   Raw CSV Dataset    |
                | (Olist E-commerce)   |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |    Extract Module    |
                |  python/extract/     |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |   Transform Module   |
                | python/transform/    |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |     Clean CSVs       |
                |    data/clean/       |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |     Load Module      |
                |    python/load/      |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |      MySQL DB        |
                |   ecommerce_etl      |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | SQL Analytics &      |
                | Validation Scripts   |
                |      sql/            |
                +----------------------+
```

---

## ETL Workflow

```text
Raw CSV Files
      │
      ▼
Extract (Python)
      │
      ▼
Transform
- Clean missing values
- Convert datetime
- Calculate revenue
- Calculate delivery days
      │
      ▼
Load (MySQL)
      │
      ▼
SQL Analytics
```

---

## Database Schema

The ETL pipeline loads transformed data into a MySQL relational database.

```text
customers
-----------
customer_id (PK)
customer_unique_id
customer_city
customer_state
...

        │
        │ customer_id
        ▼

orders
-----------
order_id (PK)
customer_id (FK)
order_status
order_purchase_timestamp
...

        │
        │ order_id
        ▼

order_items
-----------
order_id (FK)
product_id (FK)
price
freight_value
...

        ▲
        │ product_id

products
-----------
product_id (PK)
product_category_name
product_weight_g
...
```
---

## Business Questions

#### CEO — Business Overview

**Question**
- What is the overall business performance?

**Metrics**
- Total revenue
- Total orders
- Total customers
- Average order value

**SQL**
`sql/analytics/business_overview.sql`

---

#### Sales Manager — Sales Performance

**Question**
- How do sales and revenue change over time?

**SQL**
`sql/analytics/sales_trend.sql`

---

#### Logistics Manager — Delivery Performance

**Question**
- What is the average delivery time?

**SQL**
`sql/analytics/delivery_analysis.sql`

---

#### Product Performance

**Question**
- Which product categories generate the highest revenue?

**SQL**
`sql/analytics/product_analysis.sql`

---

#### Regional Sales

**Question**
- Which customer states generate the highest revenue?

**SQL**
`sql/analytics/regional_sales.sql`

---

## Repository Structure

```
data/
    raw/
    clean/

python/
    extract/
        extract_data.py
    transform/
        transform_customers.py
        transform_orders.py
        transform_products.py
        transform_order_items.py
    load/
        load_to_mysql.py
    utils/
        config.py

sql/
    analytics/
    validation/
    schema.sql

docs/

README.md
```
---

## Installation

```bash
git clone https://github.com/tanitsorn/ecommerce-etl-pipeline.git
cd ecommerce-etl-pipeline

pip install -r requirements.txt

python -m python.main
```
---

## Usage

Run the ETL pipeline:

```bash
python -m python.main
```

The pipeline will:

- Extract raw CSV files
- Transform and clean the data
- Load transformed data into MySQL
- Execute SQL analytics queries

---

## Sample Output

```
========== ETL Pipeline ==========

Step 1 : Transform

✓ Customers transformed
✓ Orders transformed
✓ Order Items transformed
✓ Products transformed

Step 2 : Load

✓ Loaded customers (99,441 rows)
✓ Loaded products (32,951 rows)
✓ Loaded orders (99,441 rows)
✓ Loaded order_items (112,650 rows)

✓ All tables loaded successfully!

ETL pipeline finished!
```

---

## Analytics SQL

#### Example Analytics Queries

##### Total Revenue

```sql
SELECT
    ROUND(SUM(price + freight_value),2) AS total_revenue
FROM order_items;
```

##### Average Delivery Time

```sql
SELECT
AVG(DATEDIFF(order_delivered_customer_date,
             order_purchase_timestamp))
AS avg_delivery_days
FROM orders;
```

##### Top Customer States

```sql
SELECT
    customer_state,
    COUNT(*) AS total_customers
FROM customers
GROUP BY customer_state
ORDER BY total_customers DESC;
```

---

## Validation SQL

#### Data Validation

##### Duplicate Check

```sql
SELECT customer_id, COUNT(*)
FROM customers
GROUP BY customer_id
HAVING COUNT(*) > 1;
```

##### Null Check

```sql
SELECT *
FROM customers
WHERE customer_id IS NULL;
```
---

## Project Status

🟢 Completed

The ETL pipeline has been fully implemented and tested.

Features:
- Extract raw ecommerce datasets
- Transform and clean data
- Load data into MySQL
- Foreign key relationships
- SQL validation scripts
- SQL analytics queries

---

## Future Improvements

- Docker
- Apache Airflow
- Unit Tests
- GitHub Actions CI/CD

---

## Acknowledgements

This project uses the following resources:

- Brazilian E-Commerce Public Dataset by Olist
  https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

- Python
- Pandas
- SQLAlchemy
- MySQL