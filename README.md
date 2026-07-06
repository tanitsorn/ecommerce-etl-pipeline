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

## Architecture

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

---

## Repository Structure

```
data/
    raw/
    clean/

python/
    extract/
        extract_date.py
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
git clone ...
cd ecommerce-etl-pipeline

pip install -r requirements.txt

python -m python.main
```
---

## Usage

---

## Sample Output

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

---

## Business Questions

* What is total revenue over time?
→ sql/analytics/revenue_analysis.sql

* Which products generate the highest revenue?
→ sql/analytics/product_analysis.sql

* Average delivery time?
→ sql/analytics/delivery_analysis.sql

---

## Analytics SQL

### Example Analytics Queries

### Total Revenue

```sql
SELECT
    ROUND(SUM(price + freight_value),2) AS total_revenue
FROM order_items;
```

### Top Customer States

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

### Data Validation

### Duplicate Check

```sql
SELECT customer_id, COUNT(*)
FROM customers
GROUP BY customer_id
HAVING COUNT(*) > 1;
```

### Null Check

```sql
SELECT *
FROM customers
WHERE customer_id IS NULL;
```

---

## Technology Stack

* Python
* Pandas
* SQL
* MySQL
* SQLAlchemy
* PyMySQL
* Git
* GitHub
* Visual Studio Code

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