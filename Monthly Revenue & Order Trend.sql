SELECT 
    DATE_FORMAT(OrderDate, '%Y-%m') AS Month,
    COUNT(OrderID) AS Total_Orders,
    SUM(TotalAmount) AS Total_Revenue,
    ROUND(AVG(TotalAmount), 2) AS Avg_Order_Value
FROM ecommerce_sales
WHERE OrderStatus = 'Delivered'
GROUP BY Month
ORDER BY Month;