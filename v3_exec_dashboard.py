import os

os.environ["FLASK_SKIP_DOTENV"] = "1"

import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output


df = pd.read_csv("SampleSuperstore.csv")

app = Dash(__name__)
app.title="Superstore Executive Dashboard"

def create_kpi_card(title, value, color):
    return html.Div(
        [html.H4(title), html.H2(value)],
        style={
            "background color": color,
            "padding": "20px",
            "borderRadius": "12px",
            "boxShadow": "0px 4px 10px rgba(0,0,0,0.2)",
            "width": "18%",
            "textAlight": "center",
            "color": "black"
        }
    )

header = html.H1(
    "Superstore Executive Dashboard",
    style={
        "textAlight": "center",
        "marginBottom": "20px"
    }
)

region_filter = dcc.Dropdown(
    id="region-dropdown",

    options=[{"label": "All regions",
              "value": "All"}] +
            [
                {"label": region,
                 "value": region}

                for region in sorted(df["Region"].unique())
            ],
    value="All",
    clearable=False
)

segment_filter = dcc.Dropdown(
    id="segment-dropdown",

    options=[{"label": "All segments",
              "value": "All"}] +
            [
                {"label": seg,
                 "value": seg}

                for seg in sorted(
                df["Segment"].unique()
            )
            ],
    value="All",
    clearable=False
)

category_filter = dcc.Dropdown(
    id="category-dropdown",

    options=[{"label": "All category",
              "value": "All"}] +
            [
                {"label": cat,
                 "value": cat}

                for cat in sorted(
                df["Category"].unique()
            )
            ],
    value="All",
    clearable=False
)

app.layout = html.Div(
    [header,
     html.Div(
         [region_filter, category_filter, segment_filter],
         style={"display": "grid",
                "gridTemplateColumns": "1fr 1fr 1fr",
                "gap": "20px"}
     ),
     html.Br(),
     html.Div(
         id="kpi-container",
         style={
             "display": "flex",
             "justifyContent": "space-between"
         }
     ),
     html.Br(),
     dcc.Graph(id="profit-category"),
     dcc.Graph(id="sales-region"),
     dcc.Graph(id="state-profit"),
     dcc.Graph(id="discount-profit"),
     html.Div(id="insight-panel")

     ],
    style={"padding": "20px",
           "backgroundColor": "#f5f7fa"}
)

@app.callback(
    [
        Output("kpi-container", "children"),
        Output("profit-category", "figure"),
        Output("sales-region", "figure"),
        Output("state-profit", "figure"),
        Output("discount-profit", "figure"),
        Output("insight-panel", "children")
    ],
    [
        Input("region-dropdown", "value"),
        Input("category-dropdown", "value"),
        Input("segment-dropdown", "value")
    ]
)

def update_dashboard(region,category,segment):
    filtered_df = df.copy()
    if region != "All":
        filtered_df = filtered_df[filtered_df["Region"] == region]
    if category != "All":
        filtered_df = filtered_df[filtered_df["Category"] == category]
    if segment != "All":
        filtered_df = filtered_df[filtered_df["Segment"] == segment]

    total_sales = (filtered_df["Sales"].sum())
    total_profit = (filtered_df["Profit"].sum())
    profit_margin = (total_profit /  total_sales * 100)
    total_orders = len(filtered_df)

    cards = [
        create_kpi_card("Sales", f"${total_sales:,.2f}","#121212"),
        create_kpi_card("Profit", f"${total_profit:,.2f}", "#121212"),
        create_kpi_card("Margin", f"${profit_margin:,.2f}", "#121212"),
        create_kpi_card("Orders",f"{total_orders}","#121212")
    ]

    category_profit = (filtered_df.groupby("Category")["Profit"].sum().reset_index())
    fig_category = px.bar(category_profit,
                          x="Category",
                          y="Profit",
                          title="Profit by Category")

    region_sales = (filtered_df.groupby("Region")["Sales"].sum().reset_index())
    fig_region = px.bar(region_sales,
                        x="Region",
                        y="Sales",
                        title="Sales by Region")

    top_states = (filtered_df.groupby("State")["Profit"].sum().sort_values(ascending=False).head(20).reset_index())
    fig_states = px.bar(top_states,
                       x="Profit",
                       y="State",
                       orientation="h",
                       title="Top 20 States")

    fig_discount = px.scatter(filtered_df,
                              x="Discount",
                              y="Profit",
                              color="Category",
                              title="Discount vs Profit")

    best_region = (filtered_df.groupby("Region")["Profit"].sum().idxmax())

    best_category = (filtered_df.groupby("Category")["Profit"].sum().idxmax())

    insight_panel = html.Div([
        html.H3("Executive Insights"),
        html.P(f"Top Region: {best_region}"),
        html.P(f"Top Category: {best_category}"),
        html.P(f"Profit Margin: {profit_margin:.2f}%")
    ])

    return(cards, fig_category, fig_region, fig_states, fig_discount, insight_panel)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)