from dash import html
import dash_bootstrap_components as dbc

SIDEBAR_STYLE = {
    "display": "flex",
    "flex-direction": "column",
    "justify-content": "space-between",
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
        html.Div([
            html.Img(src="./assets/logo.png", width=240,
                 height=95, className="rounded"),
            html.Hr(),
            dbc.Nav(
                [
                    dbc.NavLink("Explora localidades", href="/",
                                active="exact", className="rounded"),
                    dbc.NavLink("Tú perfil de turista",
                                href="/tu-perfil", active="exact", className="rounded"),
                    dbc.NavLink("Delitos en Bogotá",
                                href="/delincuencia", active="exact", className="rounded"),
                    dbc.NavLink("Sobre nosotros",
                                href="/sobre-nosotros", active="exact", className="rounded"),
                ],
                vertical=True,
                pills=True,
            ),
        ]),
        html.Div(
            html.Img(src="./assets/logo-idt-completo.png",
                     width=230, height=72),
            style={"display": "flex", "justifyContent": "center"}
        ),
    ],
    id="sidebar",
    style=SIDEBAR_STYLE
)

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Explora localidades", href="/")),
        dbc.NavItem(dbc.NavLink("Tú perfil de turista", href="/tu-perfil")),
        dbc.NavItem(dbc.NavLink("Delitos en Bogotá", href="/delincuencia")),
        dbc.NavItem(dbc.NavLink("Sobre nosotros", href="/sobre-nosotros")),
    ],
    id="navbar",
    brand="Explora Bogotá",
    brand_href="/",
    color="primary",
    dark=True,
)
