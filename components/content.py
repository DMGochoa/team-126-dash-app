from dash import Dash, dcc, html, Input, Output
from dash import html
import pandas as pd
import dash_bootstrap_components as dbc

from components.card import custom_card

df = pd.read_csv("./data-cleaned/scattermap_points.csv")

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

MARGIN_TOP = {
    "margin-top": "3rem",
}

map_controls = html.Div([
    dcc.Checklist(id='all_localidades_checkbox',
                  options={"on": "Todas las localidades"},
                  value=["on"]
                  ),
    dcc.Dropdown(id='localidad',
                 options=[{'label': str(b), 'value': b}
                          for b in sorted(df['localidad'].unique())],
                 placeholder="Selecciona una localidad",
                 style={"display": "none"}
                 ),
    dcc.Checklist(id='type',
                  options=[{'label': str(b), 'value': b}
                           for b in sorted(df['type'].unique())],
                  value=[b for b in sorted(df['type'].unique())],
                  inline=True
                  ),
    # dcc.Dropdown(id='localidad',
    #              options=[{'label': str(b), 'value': b}
    #                       for b in sorted(df['localidad'].unique())],
    #              value=[b for b in sorted(df['localidad'].unique())],
    #              multi=True
    #              ),
])

main_view = html.Div([
    dbc.Row([
        dbc.Col(custom_card("KPI #1", "Desc", "primary"), md=4),
        dbc.Col(custom_card("KPI #2", "Desc", "secondary"), md=4),
        dbc.Col(custom_card("KPI #3", "Desc", "info"), md=4)
    ]),
    dbc.Row([
        dbc.Col(map_controls, md=4, style=MARGIN_TOP),
        dbc.Col(html.Div(dcc.Graph(id="choropleth-map")),
                md=8, style=MARGIN_TOP)
    ])
])

content = html.Div(id="page-content", style=CONTENT_STYLE)
