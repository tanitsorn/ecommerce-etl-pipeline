# Transformation Mapping

## Objective

This document defines all transformation rules applied during the ETL process before loading data into MySQL.


## Customers

| Transformation | Reason |
|----------------|--------|
| Keep customer_id | Used for joining with orders |
| Keep customer_unique_id | Used for repeat customer analysis |
| Standardize customer_city (if necessary) | Improve text consistency |
| Standardize customer_state (if necessary) | Improve text consistency |


## Orders

| Transformation | Reason |
|----------------|--------|
| Convert datetime columns | Enable date calculations |
| Filter delivered orders | Exclude cancelled and unavailable orders from business analytics |
| Create delivery_days | Measure delivery performance |

Formula

delivery_days = order_delivered_customer_date - order_purchase_timestamp


## Order Items

| Transformation | Reason |
|----------------|--------|
| Create revenue | Business KPI for sales analysis |

Formula

revenue = price + freight_value


## Products

| Transformation | Reason |
|----------------|--------|
| Handle missing category | Improve data consistency |
| Handle missing metadata columns | Prevent NULL values during analysis |
| Validate product dimensions | Ensure numeric consistency |


## Final Output

The transformed dataset will support:

- Revenue Analysis
- Sales Trend Analysis
- Delivery Performance
- Top Products
- Repeat Customer Analysis