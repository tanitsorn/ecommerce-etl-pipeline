SELECT DATE(order_purchase_timestamp) AS order_date,
       COUNT(*) AS total_orders
FROM orders
GROUP BY DATE(order_purchase_timestamp)
ORDER BY order_date;