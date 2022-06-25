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
    "margin-top": "2rem",
}

map_controls = html.Div([
    html.P(
        "💡 Tip: Puedes buscar y ver localidades especificas removiendo la "
        "opción de 'Ver todas las localidades'.",
    ),
    dbc.Card(
        [
            dbc.CardImg(
                src="https://mediaim.expedia.com/destination/2/78dd6fee7217b2318c20db7cfdf68b26.jpg?impolicy=fcrop&w=360&h=224&q=mediumLow", top=True),
            dbc.CardBody(
                [
                    html.H4("Card title", className="card-title"),
                    html.P(
                        "Some quick example text to build on the card title and "
                        "make up the bulk of the card's content.",
                        className="card-text",
                    ),
                    dcc.Checklist(id='all_localidades_checkbox',
                                  options={"on": " Ver todas las localidades"},
                                  value=["on"],
                                  style={"margin-bottom": "1rem"}
                                  ),
                    dcc.Dropdown(id='localidad',
                                 options=[{'label': str(b), 'value': b}
                                          for b in sorted(df['localidad'].unique())],
                                 placeholder="Selecciona una localidad",
                                 style={"display": "none"}
                                 ),
                ]
            ),
        ]),
])

map = html.Div([
    dcc.Graph(id="choropleth-map"),
    dcc.Checklist(id='type',
                  options=[{'label': str(b), 'value': b}
                           for b in sorted(df['type'].unique())],
                  value=[b for b in sorted(df['type'].unique())],
                  inline=True,
                  labelStyle={"margin": "1rem 1rem 0 0"},
                  inputStyle={"margin-right": "0.25rem"}
                  ),

], style=MARGIN_TOP)

main_view = html.Div([
    dbc.Row([
        dbc.Col(custom_card("KPI #1", "Desc", "primary"), md=4),
        dbc.Col(custom_card("KPI #2", "Desc", "success"), md=4),
        dbc.Col(custom_card("KPI #3", "Desc", "info"), md=4)
    ]),
    dbc.Row([
        dbc.Col(map_controls, md=4, style=MARGIN_TOP),
        dbc.Col(map)
    ])
])

content = html.Div(id="page-content", style=CONTENT_STYLE)
