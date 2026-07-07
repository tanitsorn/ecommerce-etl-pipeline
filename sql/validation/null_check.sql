SELECT *
FROM orders
WHERE order_id IS NULL
    OR customer_id IS NULL;