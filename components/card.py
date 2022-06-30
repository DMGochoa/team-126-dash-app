from dash import html
import dash_bootstrap_components as dbc


def custom_card(id, title, color):
    return dbc.Card(
        dbc.CardBody(
            [
                html.H4(title, className="kpi-title"),
                html.P(className="kpi-text", id=id),
            ]
        ),
        color=color,
        className="rounded"
    )
