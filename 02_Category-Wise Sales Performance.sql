SELECT 
    Category,
    SUM(Quantity) AS Units_Sold,
    SUM(TotalAmount) AS Total_Revenue
FROM ecommerce_sales
WHERE OrderStatus = 'Delivered'
GROUP BY Category
ORDER BY Total_Revenue DESC;
