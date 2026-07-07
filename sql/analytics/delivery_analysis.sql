SELECT ROUND(AVG(
    DATEDIFF(order_delivered_customer_date, order_purchase_timestamp))
    , 2) AS avg_delivery_days
FROM orders
WHERE order_status ='delivered';