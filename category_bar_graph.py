import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("SampleSuperstore.csv")

#Bar graph for Categories
category_profit = (
    df.groupby('Category')['Profit']
    .sum()
    .sort_values(ascending=False)
)

category_profit.plot(kind='bar')
plt.title('Profit by Category')
plt.ylabel('Profit')
plt.show()

df[['Discount','Profit']].corr()

plt.scatter(df['Discount'], df['Profit'])
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.title("Profit vs Discounts")
plt.show()