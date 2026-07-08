-- ==================================================
-- Business Question:
-- What is the average delivery time?
-- Are there delayed deliveries?
--
-- Metrics:
-- - Average delivery days
-- - Number of delayed orders
-- - Percentage of delayed orders
-- ==================================================

SELECT COUNT(*) AS total_delivered_orders,
       ROUND(AVG(DATEDIFF(
                    order_delivered_customer_date, order_purchase_timestamp)
                ) , 2) AS avg_delivery_days,
       SUM(CASE
            WHEN order_delivered_customer_date > order_estimated_delivery_date THEN 1
            ELSE 0
            END) AS delayed_orders,
       ROUND(SUM(CASE
                    WHEN order_delivered_customer_date > order_estimated_delivery_date THEN 1
                    ELSE 0
                    END) * 100 / COUNT(*) 
                    , 2) AS delayed_percentage
FROM orders
WHERE order_status = 'delivered';