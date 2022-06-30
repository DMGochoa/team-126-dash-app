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
        html.Img(src="./assets/logo.png", width=240, height=95, className="rounded"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Explora localidades", href="/", active="exact", className="rounded"),
                dbc.NavLink("Tú perfil de turista",
                            href="/tu-perfil", active="exact", className="rounded"),
                dbc.NavLink("Delitos en Bogotá",
                            href="/delincuencia", active="exact", className="rounded"),
                dbc.NavLink("Sobre nosotros",
                            href="/sobre-nosotros", active="exact", className="rounded"),
            ],
            vertical=True,
            pills=True,
        )
    ],
    id="sidebar",
    style=SIDEBAR_STYLE
)
