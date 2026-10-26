import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("SampleSuperstore.csv")

df[['Discount','Profit']].corr()

plt.scatter(df['Discount'], df['Profit'])
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.title("Profit vs Discounts")
plt.show()