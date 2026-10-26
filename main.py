import pandas as pd
import matplotlib.pyplot as plt

#import dataset
df = pd.read_csv("SampleSuperstore.csv")

#view the columns, types and how many items have null values
# print(df.head())
# print(df.info())

#summary statistics (postal code, sales, quantity, discount, profit)
# print(df.describe())

#Business KPI's
print(f"Total Sales: ${df['Sales'].sum():,.2f}")
print(f"Total Profit: ${df['Profit'].sum():,.2f}")
profit_margin = (df['Profit'].sum() / df['Sales'].sum()) * 100
print(f"Profit Margin: {profit_margin:.2f}%")

"""which category makes the most money
method chaining- pandas library
each method operates on the result by the previous operands """
category_profit = (
    df.groupby('Category')['Profit']
    .sum()
    .sort_values(ascending=False)
)
print(category_profit)

category_profit.plot(kind='bar')
plt.title('Profit by Category')
plt.ylabel('Profit')
plt.show()