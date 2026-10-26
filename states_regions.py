import pandas as pd
import matplotlib.pyplot as plt

#import dataset
df = pd.read_csv("SampleSuperstore.csv")

#Sales by Region
sales_by_region = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)
print(sales_by_region)

profit_by_region = (
    df.groupby('Region')['Profit']
    .sum()
    .sort_values(ascending=False)
)
print(profit_by_region)

print("Top 10 Best Selling States")
profit_by_state = (
    df.groupby('State')['Profit']
    .sum()
    .sort_values(ascending=False)
)
print(profit_by_state.head(10))
print("Top 10 Worst Selling States")
print(profit_by_state.tail(10))


top_states = (
    df.groupby("State")["Profit"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
top_states.plot(
    kind="barh",
    figsize=(10,6),
    color="teal"
)

plt.title("Top 10 States by Profit")
plt.xlabel("Profit ($)")
plt.show()

bottom_states = (
    df.groupby("State")["Profit"]
    .sum()
    .sort_values()
    .head(10)
)
bottom_states.plot(
    kind="barh",
    figsize=(10,6),
    color="red"
)
plt.title("Bottom 10 States by Profit")
plt.xlabel("Profit ($)")
plt.show()
