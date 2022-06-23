from dash import Dash, dcc, html, Input, Output
from dash import html
import pandas as pd
import dash_bootstrap_components as dbc

from components.card import card

df = pd.read_csv("./data-cleaned/scattermap_points.csv")

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

right_column = html.Div(
    [
        dcc.Checklist(id='type',
                      options=[{'label': str(b), 'value': b}
                               for b in sorted(df['type'].unique())],
                      value=[b for b in sorted(df['type'].unique())],
                      inline=True
                      ),
        dcc.Dropdown(id='localidad',
                     options=[{'label': str(b), 'value': b}
                              for b in sorted(df['localidad'].unique())],
                     value=[b for b in sorted(df['localidad'].unique())],
                     multi=True
                     ),
        dcc.Graph(id="choropleth-map"),
    ]
)

left_column = html.Div([
    dbc.Row([card])  # , table])
])

table = dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)

main_view = html.Div([
    html.H4('Bogotá'),
    html.P("Selecciona una de las opciones:"),
    dbc.Row([
        dbc.Col(left_column, md=4),
        dbc.Col(right_column, md=8)
    ])
])

content = html.Div(id="page-content", style=CONTENT_STYLE)
