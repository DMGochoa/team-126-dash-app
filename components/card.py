from dash import html
import dash_bootstrap_components as dbc

card = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Title", className="card-title"),
            html.P(
                "Some quick example text to build on the card title and make "
                "up the bulk of the card's content.",
                className="card-text",
            ),
        ]
    ),
    color="dark",
    outline=True
)
