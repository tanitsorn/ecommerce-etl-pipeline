SELECT ROUND(SUM(price + freight_value), 2) AS total_revenue
FROM order_items;