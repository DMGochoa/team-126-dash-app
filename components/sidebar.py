from dash import html
import dash_bootstrap_components as dbc

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

sidebar = html.Div(
    [
        html.H2("Team 126", className="display-4"),
        html.Hr(),
        # html.P(
        #     "A simple sidebar layout with navigation links", className="lead"
        # ),
        dbc.Nav(
            [
                dbc.NavLink("Explora Bogotá",
                            href="/", active="exact"),
                dbc.NavLink("Tú perfil de turista",
                            href="/page-1", active="exact"),
                dbc.NavLink("Sobre nosotros", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        )
    ],
    style=SIDEBAR_STYLE
)
