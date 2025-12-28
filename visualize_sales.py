import pandas as pd
import matplotlib.pyplot as plt
import os

# Create output folder
os.makedirs("output", exist_ok=True)

# Load data
data = pd.read_csv("sales_data.csv")

# Monthly sales total
monthly_sales = data.groupby("Month")["Sales"].sum()

# Category sales total
category_sales = data.groupby("Category")["Sales"].sum()

# Plot 1: Monthly Sales
plt.figure()
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid()
plt.savefig("output/monthly_sales.png")
plt.show()

# Plot 2: Category-wise Sales
plt.figure()
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.savefig("output/category_sales.png")
plt.show()
