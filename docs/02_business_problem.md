# Business Problem

## Background

Many e-commerce companies collect large amounts of transactional data every day. However, raw operational data is often difficult to use directly for business analysis because it contains inconsistent formats, missing values, and information spread across multiple tables.

Without a structured ETL pipeline, decision makers spend significant time preparing data instead of analyzing it.


## Business Problems

### 1. Revenue Visibility

Management cannot quickly monitor overall sales performance because revenue-related information is distributed across multiple tables.


### 2. Delivery Performance

The company needs to measure delivery speed to evaluate logistics performance and customer satisfaction.


### 3. Product Performance

Business users require product-level sales insights to identify top-performing products and categories.


### 4. Customer Analysis

The business wants to identify repeat customers for future customer retention strategies.


## Proposed Solution

Build an ETL pipeline that:

* Extracts raw transactional data
* Cleans and standardizes datasets
* Creates business metrics such as Revenue and Delivery Days
* Loads transformed data into MySQL
* Supports SQL-based business analytics
