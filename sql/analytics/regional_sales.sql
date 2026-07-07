SELECT c.customer_state,
       ROUND(SUM(oi.price + oi.freight_value) , 2) AS revenue
FROM customers c 
JOIN orders o 
ON c.customer_id = o.customer_id
JOIN order_items oi 
ON o.order_id = oi.order_id
GROUP BY c.customer_state
ORDER BY revenue DESC;