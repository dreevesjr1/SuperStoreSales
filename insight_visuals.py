import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("SampleSuperstore.csv")

#Discount vs Profit
df[['Discount','Profit']].corr()
plt.scatter(df['Discount'], df['Profit'], alpha=0.4)
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.title("Discount vs Profit")
plt.show()

#Sales Distribution
plt.figure(figsize=(10,6))
plt.hist(df['Sales'], bins=30)
plt.title("Distribution of Sales")
plt.xlabel("Sale Amount")
plt.ylabel("Frequency")
plt.show()

#Profit Distribution
plt.figure(figsize=(10,6))
plt.hist(df['Profit'], bins=30)
plt.title("Distribution of Profits")
plt.xlabel("Profit")
plt.ylabel("Frequency")
plt.show()