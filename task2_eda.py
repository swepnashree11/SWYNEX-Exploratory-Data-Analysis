import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Load cleaned dataset
file_path = Path("data/processed/dirty_cafe_sales_cleaned_v2.csv")
df = pd.read_csv(file_path)

# Convert Transaction Date to datetime
df["Transaction Date"] = pd.to_datetime(
    df["Transaction Date"],
    errors="coerce"
)

# Display basic dataset information
print("========== DATASET OVERVIEW ==========")
print("Dataset Shape:", df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nFirst 5 Rows:")
print(df.head())

# Descriptive Statistics
print("\n========== NUMERICAL STATISTICS ==========")

print(df[["Quantity", "Price Per Unit", "Total Spent"]].describe())

# Sales Summary
print("\n========== SALES SUMMARY ==========")

total_revenue = df["Total Spent"].sum()
average_transaction = df["Total Spent"].mean()
median_transaction = df["Total Spent"].median()
total_transactions = df["Transaction ID"].nunique()

print("Total Transactions:", total_transactions)
print("Total Revenue:", total_revenue)
print("Average Transaction Value:", round(average_transaction, 2))
print("Median Transaction Value:", median_transaction)

# Category-wise sales
print("\n========== ITEM-WISE SALES ==========")

item_sales = df.groupby("Item")["Total Spent"].sum().sort_values(ascending=False)
print(item_sales)

# Payment Method Analysis
print("\n========== PAYMENT METHOD ANALYSIS ==========")

payment_analysis = df.groupby("Payment Method").agg(
    Transactions=("Transaction ID", "count"),
    Revenue=("Total Spent", "sum")
).sort_values("Transactions", ascending=False)

print(payment_analysis)

# Location Analysis
print("\n========== LOCATION ANALYSIS ==========")

location_analysis = df.groupby("Location").agg(
    Transactions=("Transaction ID", "count"),
    Revenue=("Total Spent", "sum")
).sort_values("Revenue", ascending=False)

print(location_analysis)

# Create visualization folder
output_folder = Path("task2_visualizations")
output_folder.mkdir(exist_ok=True)

# Chart 1: Revenue by Item
item_revenue = (
    df[df["Item"] != "Unknown"]
    .groupby("Item")["Total Spent"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
item_revenue.plot(kind="bar")
plt.title("Total Revenue by Item")
plt.xlabel("Item")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(output_folder / "revenue_by_item.png")
plt.close()

# Chart 2: Transactions by Payment Method
payment_counts = df["Payment Method"].value_counts()

plt.figure(figsize=(8, 6))
payment_counts.plot(kind="bar")
plt.title("Transactions by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Number of Transactions")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(output_folder / "payment_method.png")
plt.close()

print("\nFirst two charts saved successfully!")


# Chart 3: Monthly Revenue Trend

monthly_sales = (
    df.dropna(subset=["Transaction Date"])
    .groupby(df.dropna(subset=["Transaction Date"])["Transaction Date"].dt.month)["Total Spent"]
    .sum()
)

plt.figure(figsize=(10, 6))
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Revenue Trend - 2023")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.xticks(
    range(1, 13),
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
)
plt.grid(True)
plt.tight_layout()

plt.savefig(output_folder / "monthly_revenue_trend.png")
plt.close()

print("Monthly revenue chart saved successfully!")
print("\nMonthly Revenue:")
print(monthly_sales)


# Anomaly Detection using IQR Method

print("\n========== ANOMALY DETECTION ==========")

sales = df["Total Spent"].dropna()

Q1 = sales.quantile(0.25)
Q3 = sales.quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = sales[
    (sales < lower_limit) |
    (sales > upper_limit)
]

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Limit:", lower_limit)
print("Upper Limit:", upper_limit)
print("Number of Outliers:", len(outliers))

print("\nOutlier Values:")
print(outliers.head(10))


# Chart 4: Sales Outlier Detection

plt.figure(figsize=(8, 6))

plt.boxplot(sales)

plt.title("Box Plot - Total Spent Outlier Detection")
plt.ylabel("Total Spent")

plt.tight_layout()
plt.savefig(output_folder / "sales_outliers.png")
plt.close()

print("Outlier chart saved successfully!")