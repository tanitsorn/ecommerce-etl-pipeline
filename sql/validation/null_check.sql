SELECT *
FROM orders
WHERE order_od IS NULL
    OR customer_id IS NULL;