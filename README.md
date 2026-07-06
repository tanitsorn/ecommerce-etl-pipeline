# E-commerce ETL Pipeline

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

Brazilian E-Commerce Public Dataset by Olist

Tables used:

* Customers
* Orders
* Order Items
* Products

---

## Technology Stack

* Python
* Pandas
* SQL
* MySQL
* Git
* GitHub
* Visual Studio Code

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

## Business Questions

* What is the total revenue over time?
* Which products generate the highest revenue?
* What is the average delivery time?
* How many repeat customers does the business have?

---

## Repository Structure

```
data/
    raw/
    clean/

python/
    extract/
    transform/
    load/
    utils/

sql/
    analytics/
    validation/

docs/

README.md
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