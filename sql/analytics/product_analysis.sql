-- ==================================================
-- Business Question:
-- Which product categories generate the highest revenue?
--
-- Metrics:
-- - Total items sold
-- - Revenue by product category
-- ==================================================

SELECT p.product_category_name,
       count(*) AS total_items_sold,
       ROUND(SUM(oi.price), 2) AS revenue
FROM order_items oi 
JOIN products p 
ON oi.product_id = p.product_id
GROUP BY p.product_category_name
ORDER BY revenue DESC
LIMIT 10;