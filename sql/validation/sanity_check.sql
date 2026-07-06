-- Negative price
SELECT *
FROM order_items
WHERE price < 0;

-- Negative freight
SELECT *
FROM order_items
WHERE freight_value < 0;

-- Invalid delivery date
SELECT *
FROM orders
WHERE order_delivered_customer_date <
      order_purchase_timestamp;