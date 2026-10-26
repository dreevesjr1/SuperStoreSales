import pandas as pd
import matplotlib.pyplot as plt

#import dataset
df = pd.read_csv("SampleSuperstore.csv")

"""which category makes the most money
method chaining- pandas library
each method operates on the result by the previous operands """
category_profit = (
    df.groupby('Category')['Profit']
    .sum()
    .sort_values(ascending=False)
)
# print(category_profit)

category_profit.plot(kind='bar')
plt.title('Profit by Category')
plt.ylabel('Profit')
plt.show()

#Profitable Sub-Category
subcategory_profit = (
    df.groupby('Sub-Category')['Profit']
    .sum()
    .sort_values()
)
print(subcategory_profit.head(10))

#Unprofitable Sub-Category
losses = (
    df.groupby("Sub-Category")["Profit"]
    .sum()
    .sort_values()
)
print(losses.head(10))