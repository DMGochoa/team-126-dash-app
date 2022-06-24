from dash import html
import dash_bootstrap_components as dbc


def custom_card(title, description, color):
    return dbc.Card(
        dbc.CardBody(
            [
                html.H4(title, className="card-title"),
                html.P(
                    description,
                    className="card-text",
                ),
            ]
        ),
        color=color,
        outline=True
    )
