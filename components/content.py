from random import randrange
from dash import dcc, html
import pandas as pd
import dash_bootstrap_components as dbc

from components.card import custom_card

df = pd.read_csv("./data-cleaned/scattermap_points.csv")
localidad_list = sorted(df['localidad'].unique())
localidad_list.remove('MUNICIPIOS ALEDAÑOS')

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

MARGIN_TOP = {
    "margin-top": "2rem",
}

RANDOM_TIPS = [
    "💡 Tip: Si quieres conocer más sobre este proyecto puedes hacer clic en 'Sobre nosotros' en la barra lateral.",
    "💡 Tip: Las tarjetas con KPI cambian para mostrar información sobre la localidad seleccionada."
]

map_controls = html.Div([
    html.P(
        RANDOM_TIPS[randrange(len(RANDOM_TIPS))]
    ),
    dbc.Card(
        [
            dbc.CardImg(
                src="https://mediaim.expedia.com/destination/2/78dd6fee7217b2318c20db7cfdf68b26.jpg?impolicy=fcrop&w=360&h=224&q=mediumLow", top=True),
            dbc.CardBody(
                [
                    html.H4("Comienza a explorar", className="card-title"),
                    html.P(
                        "Puedes buscar y ver localidades especificas removiendo la "
                        "opción de 'Ver todas las localidades'.",
                        className="card-text",
                    ),
                    dcc.Checklist(id='all_localidades_checkbox',
                                  options={"on": " Ver todas las localidades"},
                                  value=["on"],
                                  style={"margin-bottom": "1rem"}
                                  ),
                    dcc.Dropdown(id='localidad',
                                 options=[{'label': str(b), 'value': b}
                                          for b in localidad_list],
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
        dbc.Col(custom_card("kpi_crime", "🚨 Crimen", "primary"), md=4),
        dbc.Col(custom_card("kpi_mean_hotel_price",
                "🏨 Hoteles", "success"), md=4),
        dbc.Col(custom_card("kpi_number_of_touristic_attractions",
                "🏕 Turismo", "info"), md=4)
    ]),
    dbc.Row([
        dbc.Col(map_controls, md=4, style=MARGIN_TOP),
        dbc.Col(map, md=8)
    ])
])

content = html.Div(id="page-content", style=CONTENT_STYLE)
