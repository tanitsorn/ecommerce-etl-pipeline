SELECT DATE(order_purchase_timestamp) AS order_date,
       COUNT(DISTINCT o.order_id) AS total_orders,
       ROUND(SUM(price + freight_value) , 2) AS daily_revenue
FROM orders o 
JOIN order_items oi 
ON o.order_id = oi.order_id
GROUP BY DATE(order_purchase_timestamp)
ORDER BY order_date;