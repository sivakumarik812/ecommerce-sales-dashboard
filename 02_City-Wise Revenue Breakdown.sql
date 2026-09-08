SELECT 
    City,
    COUNT(OrderID) AS Total_Orders,
    SUM(TotalAmount) AS Total_Revenue
FROM ecommerce_sales
WHERE OrderStatus = 'Delivered'
GROUP BY City
ORDER BY Total_Revenue DESC;
