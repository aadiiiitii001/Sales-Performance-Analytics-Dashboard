import pandas as pd
import random
from datetime import datetime, timedelta

# Number of records
N = 5000

products = [
    (1, "Laptop", "Electronics", "Computers"),
    (2, "Headphones", "Electronics", "Audio"),
    (3, "Shoes", "Fashion", "Footwear"),
    (4, "Watch", "Fashion", "Accessories"),
    (5, "Mobile", "Electronics", "Phones")
]

segments = ["Retail", "Wholesale", "Enterprise"]

regions = ["North", "South", "East", "West"]

data = []

for i in range(N):
    product = random.choice(products)
    customer_id = random.randint(1000, 2000)
    segment = random.choice(segments)
    date = datetime.now() - timedelta(days=random.randint(1, 365))
    quantity = random.randint(1, 10)
    price = random.randint(1000, 50000)
    revenue = quantity * price

    data.append([
        i + 1,
        product[0],
        customer_id,
        date.strftime("%Y-%m-%d"),
        quantity,
        price,
        revenue,
        random.choice(regions),
        product[1],
        product[2],
        product[3],
        f"Customer {customer_id}",
        segment
    ])

df = pd.DataFrame(data, columns=[
    "SaleID", "ProductID", "CustomerID", "Date",
    "Quantity", "UnitPrice", "Revenue", "Region",
    "ProductName", "Category", "SubCategory",
    "CustomerName", "Segment"
])

df.to_csv("sales_data.csv", index=False)

print("sales_data.csv generated successfully!")
