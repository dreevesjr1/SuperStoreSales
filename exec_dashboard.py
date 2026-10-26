import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("SampleSuperstore.csv")

#KPI's
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
profit_margin = (total_profit / total_sales) * 100
total_orders = len(df)

best_region = (
    df.groupby('Region')['Profit']
    .sum()
    .idxmax()
)

best_category = (
    df.groupby('Category')['Profit']
    .sum()
    .idxmax()
)

#Summary statistics
category_profit = df.groupby('Category')['Profit'].sum()
region_sales = df.groupby('Region')['Sales'].sum()
segment_profit = df.groupby('Segment')['Profit'].sum()
top_states = (
    df.groupby('State')['Profit']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

# Create Dashboard
fig = plt.figure(figsize=(18,12))

fig.text(0.05,0.095, f"Total Sales\n${total_sales:.0f}",
         fontsize=16, bbox=dict(facecolor='lightblue'))
fig.text(0.25,0.095, f"Total Profit\n${total_profit:.0f}",
         fontsize=16, bbox=dict(facecolor='lightgreen'))
fig.text(0.45,0.95,f"Profit Margin\n{profit_margin:.2f}%",
         fontsize=16, bbox=dict(facecolor='khaki'))
fig.text(0.65, 0.95, f"Orders\n{total_orders:,}",
         fontsize=16, bbox=dict(facecolor='lavender'))
fig.text(0.83, 0.95, f"Best Region\n{best_region}",
         fontsize=16,bbox=dict(facecolor='mistyrose'))

#Charts
#Category Profit
ax1 = plt.subplot(231)
category_profit.plot(
    kind='bar',
    color='steelblue',
    ax = ax1
)
ax1.set_title("Profit by Category")
ax1.set_ylabel("Profit")

#Sales by Region
ax2 = plt.subplot(232)
region_sales.plot(
    kind='bar',
    color='orange',
    ax=ax2
)
ax2.set_title("Sales by Region")
ax2.set_ylabel("Sales")

#Profit by Segment
ax3 = plt.subplot(233)
segment_profit.plot(
    kind='bar',
    color='purple',
    ax=ax3
)
ax3.set_title("Profit by Segment")
ax3.set_ylabel("Profit")

#Top States
ax4 = plt.subplot(234)
top_states.plot(
    kind='barh',
    color='green',
    ax=ax4
)
ax4.set_title("Top 10 States by Profit")

#Discount vs Profit
ax5 = plt.subplot(235)
ax5.scatter(df['Discount'], df['Profit'], alpha = 0.4)
ax5.set_title("Discount vs Profit")
ax5.set_xlabel("Discount")
ax5.set_ylabel("Profit")

#Sales Distribution
ax6 = plt.subplot(236)
ax6.hist(
    df['Sales'], bins=30, color='skyblue'
)
ax6.set_title("Sales Distribution")
ax6.set_xlabel("Sales")

plt.tight_layout(rect=[0,0,1,0.9])

plt.show()