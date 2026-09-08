SELECT 
    PaymentMethod,
    COUNT(OrderID) AS Total_Transactions,
    SUM(TotalAmount) AS Total_Amount
FROM ecommerce_sales
GROUP BY PaymentMethod
ORDER BY Total_Amount DESC;