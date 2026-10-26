import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("SampleSuperstore.csv")

#Total Sales
total_sales = df['Sales'].sum()

plt.figure(figsize=(6,3))
plt.text(0.5, 0.5,
         f"${total_sales:,.0f}",
         fontsize=32,
         ha='center')

plt.title("Total Sales")
plt.axis('off')
plt.show()

#Total Profit
total_profit = df['Profit'].sum()
plt.figure(figsize=(6,3))
plt.text(0.5, 0.5,
         f"${total_profit:,.0f}",
         fontsize=32,
         color='green',
         ha='center')
plt.title("Total Profit")
plt.axis('off')
plt.show()

#Profit by Category
category_profit = (
    df.groupby("Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)
category_profit.plot(
    kind="bar",
    figsize=(8,5),
    color='steelblue'
)
plt.title("Profit by Category")
plt.ylabel("Profit ($)")
plt.xlabel("Category")
plt.show()

#Sales by Region
region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)
region_sales.plot(
    kind="bar",
    figsize=(8,5),
    color="orange"
)
plt.title("Sales by Region")
plt.ylabel("Sales ($)")
plt.xlabel("Region")
plt.show()

#Profit by Region
region_profit = (
    df.groupby("Region")["Profit"]
    .sum()
    .sort_values(ascending=False)
)
region_profit.plot(
    kind="bar",
    figsize=(8,5),
    color="green"
)
plt.title("Profit by Region")
plt.ylabel("Profit ($)")
plt.xlabel("Region")
plt.show()

#Profit by Customer Segment
segment_profit = (
    df.groupby("Segment")["Profit"]
    .sum()
    .sort_values(ascending=False)
)
segment_profit.plot(
    kind="bar",
    figsize=(8,5),
    color="purple"
)
plt.title("Profit by Customer Segment")
plt.ylabel("Profit ($)")
plt.xlabel("Segment")
plt.show()

#Sales by Category
sales_by_category = (
    df.groupby("Category")["Sales"]
    .sum()
)
sales_by_category.plot(
    kind="pie",
    autopct='%1.1f%%',
    figsize=(8,8)
)
plt.title("Sales Distribution by Category")
plt.ylabel("")
plt.show()
