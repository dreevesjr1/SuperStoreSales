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
print(category_profit)

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

#Segment profits
segment_profit = (
    df.groupby('Segment')['Profit']
    .sum()
    .sort_values(ascending=False)
)
print(segment_profit)

#Shipping profit breakdown
ship_profit = (
    df.groupby('Ship Mode')['Profit']
    .sum()
    .sort_values(ascending=False)
)
print(ship_profit)