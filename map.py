from dash import Dash, dcc, html, Input, Output
from urllib.request import urlopen
import pandas as pd
import plotly.express as px
import json
import plotly.graph_objects as go

app = Dash(__name__)

server = app.server

app.layout = html.Div([
    html.H4('Bogotá'),
    html.P("Selecciona una de las opciones:"),
    dcc.RadioItems(
        id='map_option',
        options={
            "localidad": "Localidad",
            "puntos_wifi_count": "Puntos WiFi (Heatmap)"
        },
        value="localidad",
        inline=True
    ),
    dcc.Graph(id="choropleth-map"),
])


@app.callback(
    Output("choropleth-map", "figure"),
    Input("map_option", "value"))
def display_choropleth(map_option):
    # Load geojson and csv
    df = pd.read_csv("./data/wifi-hotspots-per-location-fake.csv")
    with open("./data/poligonos-localidades-v2.geojson") as response:
        geojson = json.load(response)

    # Map choropleth map exactly how you would do it on a jupyter notebook
    # using plotly express
    fig = px.choropleth(
        df, geojson=geojson, color=map_option,
        locations="localidad", featureidkey="properties.Nombre de la localidad")
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
