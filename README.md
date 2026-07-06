# E-commerce ETL Pipeline

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.x-green)
![MySQL](https://img.shields.io/badge/MySQL-8-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

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

## Installation

---

## Usage

---

# Sample Output

---

## Business Questions

* What is the total revenue over time?
* Which products generate the highest revenue?
* What is the average delivery time?
* How many repeat customers does the business have?

---

## Analytics SQL

---

## Validation SQL

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

---

## Acknowledgements