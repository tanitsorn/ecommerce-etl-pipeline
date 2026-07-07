SELECT c.customer_state,
       ROUND(AVG(oi.freight_value), 2) AS avg_freight_cost
FROM customers c 
JOIN orders o
ON c.customer_id = o.customer_id
JOIN order_items oi 
ON o.order_id = oi.order_id
GROUP BY c.customer_state
ORDER BY avg_freight_cost DESC;