
import pandas as pd
import numpy as np

from pathlib import Path

# Project Folder Location
BASE_DIR = Path(__file__).resolve().parent.parent

# Cleaned Dataset Location
file_path = BASE_DIR / "Dataset" / "Superstore_Cleaned.csv"

# Load Dataset
df = pd.read_csv(file_path, parse_dates=["Order Date", "Ship Date"])

print("Cleaned Dataset Loaded Successfully!")

print(df.head())

# Total Sales
total_sales = df["Sales"].sum()

# Total Profit
total_profit = df["Profit"].sum()

# Total Orders
total_orders = df["Order ID"].nunique()

# Total Customers
total_customers = df["Customer ID"].nunique()

# Total Products
total_products = df["Product ID"].nunique()

print("\n----- SALES SUMMARY -----")

print("Total Sales:", round(total_sales, 2))
print("Total Profit:", round(total_profit, 2))
print("Total Orders:", total_orders)
print("Total Customers:", total_customers)
print("Total Products:", total_products)
