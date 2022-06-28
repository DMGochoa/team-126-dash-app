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
        # html.H2("Team 126", className="display-4"),
        # dbc.CardImg(
        #                     src='https://drive.google.com/uc?export=view&id=1Nlm913gMywW1-Bvvc7PNRnc5ZV5OsI4a',
        #                     className="img-fluid rounded-start",
        #                 ),

        html.Img(src="./assets/logo.png", width=250, height=100),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Explora localidades", href="/", active="exact"),
                dbc.NavLink("Tú perfil de turista",
                            href="/tu-perfil", active="exact"),
                dbc.NavLink("Delitos en Bogotá",
                            href="/delincuencia", active="exact"),
                dbc.NavLink("Sobre nosotros",
                            href="/sobre-nosotros", active="exact"),
            ],
            vertical=True,
            pills=True,
        )
    ],
    id="sidebar",
    style=SIDEBAR_STYLE
)
