import pandas as pd
import plotly.express as px
import os

os.environ["FLASK_SKIP_DOTENV"] = "1"

from dash import Dash, html, dcc, Input, Output


df = pd.read_csv("SampleSuperstore.csv")

total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
profit_margin = (total_profit / total_sales) * 100
total_order = len(df)

#Visuals
category_profit = (
    df.groupby('Category')['Profit']
    .sum()
    .reset_index()
)
fig_category = px.bar(
    category_profit,
    x="Category",
    y="Profit",
    title="Profit by Category"
)

region_sales = (
    df.groupby('Region')['Sales']
    .sum()
    .reset_index()
)
fig_region = px.bar(
    region_sales,
    x="Region",
    y="Sales",
    title="Sales by Region"
)

fig_discount = px.scatter(
    df, x="Discount", y="Profit",
    color="Category", title="Discount vs Profit"
)

app = Dash(__name__)
app.layout = html.Div([

    html.H1("Super Store Executive Dashboard"),

    html.Div([
        html.Div([html.H3("Total Sales"),
                  html.H2(f"${total_sales:,.0f}")]),
        html.Div([html.H3("Total Profit"),
                  html.H2(f"${total_profit:,.0f}")]),
        html.Div([html.H3("Profit Margin"),
                  html.H2(f"${profit_margin:,.0f}")]),
        html.Div([html.H3("Numer of Orders"),
                  html.H2(f"${total_order:,.0f}")])
                 ],
    style={
        "display":"flex",
        "justifyContent":"space-around"
    }),

    dcc.Graph(figure=fig_category),
    dcc.Graph(figure=fig_region),
    dcc.Graph(figure=fig_discount)
])

if __name__ == "__main__":
    app.run(debug=True,
            use_reloader=False)