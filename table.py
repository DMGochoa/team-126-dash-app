from dash import Dash, dcc, html, Input, Output
import os


external_stylesheets = ['table.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server


app.layout = html.Div(
    html.Table([
        html.Thead(
            html.Tr(
                html.Th("The table header",colSpan=2)
            )
        ),
        html.Tbody(
            html.Tr([
                html.Td("The table body"),
                html.Td("With two columns")
            ])
        )
    ])
)

if __name__ == '__main__':
    app.run_server(debug=True)