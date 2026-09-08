import pandas as pd
import numpy as np

# Set random seed
np.random.seed(42)

n_orders = 1200
order_ids = range(1001, 1001 + n_orders)
dates = pd.date_range(start='2025-01-01', end='2025-12-31', periods=n_orders)
np.random.shuffle(dates.values)

customer_ids = np.random.randint(501, 750, size=n_orders)

categories_products = {
    'Electronics': [('Smartphone', 25000), ('Laptop', 55000), ('Wireless Earbuds', 2500), ('Smartwatch', 4500)],
    'Clothing': [('T-Shirt', 799), ('Jeans', 1899), ('Jacket', 3499), ('Hoodie', 2199)],
    'Footwear': [('Running Shoes', 3299), ('Sneakers', 2799), ('Formal Shoes', 3999)],
    'Home & Kitchen': [('Coffee Maker', 4999), ('Blender', 2999), ('Air Fryer', 6999)]
}

cities = ['Hyderabad', 'Bangalore', 'Chennai', 'Mumbai', 'Delhi', 'Pune']
city_weights = [0.25, 0.25, 0.15, 0.15, 0.10, 0.10]
payment_methods = ['UPI', 'Credit Card', 'Debit Card', 'COD']
payment_weights = [0.45, 0.30, 0.15, 0.10]
order_statuses = ['Delivered', 'Cancelled', 'Returned']
status_weights = [0.85, 0.08, 0.07]

data = []
for i in range(n_orders):
    cat = np.random.choice(list(categories_products.keys()))
    prod, price = categories_products[cat][np.random.randint(0, len(categories_products[cat]))]
    qty = np.random.choice([1, 2, 3, 4], p=[0.6, 0.25, 0.1, 0.05])
    city = np.random.choice(cities, p=city_weights)
    pay = np.random.choice(payment_methods, p=payment_weights)
    status = np.random.choice(order_statuses, p=status_weights)
    
    data.append({
        'OrderID': order_ids[i],
        'OrderDate': dates[i].strftime('%Y-%m-%d'),
        'CustomerID': customer_ids[i],
        'Category': cat,
        'ProductName': prod,
        'UnitPrice': price,
        'Quantity': qty,
        'TotalAmount': price * qty,
        'City': city,
        'PaymentMethod': pay,
        'OrderStatus': status
    })

df = pd.DataFrame(data)
df.sort_values(by='OrderDate', inplace=True)

# Save to CSV
df.to_csv('ecommerce_sales_dataset.csv', index=False)
print("CSV File Generated Successfully!")
