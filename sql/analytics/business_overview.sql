SELECT COUNT(DISTINCT o.order_id) AS total_orders,
       COUNT(DISTINCT c.customer_id) AS total_customers,
       ROUND(SUM(oi.price + oi.freight_value), 2) AS total_revenue,
       ROUND(SUM(oi.price + oi.freight_value)
       / COUNT(DISTINCT o.order_id) , 2) AS average_order_value
FROM orders o
JOIN customers c
ON o.customer_id = c.customer_id
JOIN order_items oi 
ON o.order_id = oi.order_id;