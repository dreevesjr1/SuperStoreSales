import os

os.environ["FLASK_SKIP_DOTENV"] = "1"

import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output


df = pd.read_csv("SampleSuperstore.csv")

app = Dash(__name__)
app.title="Superstore Executive Dashboard"

def create_api_card(title, value, color):
    return html.Div(
        [html.H4(title), html.H2(value)],
        style={
            "background color": color,
            "padding": "20px",
            "borderRadius": "12px",
            "boxShadow": "0px 4px 10px rgba(0,0,0,0.2)",
            "width": "18%",
            "textAlight": "center",
            "color": "white"
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
           "backgroundColor": "#F5F7FA"}
)

app.callback(
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

    