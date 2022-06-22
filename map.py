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
    dcc.Checklist(
        ['New York City', 'Montréal', 'San Francisco'],
        ['new_york_city', 'montreal'],
        inline=True
    ),
    dcc.Graph(id="choropleth-map"),
])


@app.callback(
    Output("choropleth-map", "figure"),
    Input("map_option", "value"))
def display_choropleth(map_option):
    # Load geojson and csv
    wifi_hotspots = pd.read_csv("./data/wifi-hotspots-per-location-fake.csv")
    bogota_malls = pd.read_csv(
        "https://raw.githubusercontent.com/andrescuco/team-126-dash-app/master/data/bogota_malls.csv")

    with open("./data-cleaned/poligonos-localidades-v2.geojson") as response:
        bogota_geojson = json.load(response)

    # Map choropleth map exactly how you would do it on a jupyter notebook
    fig = px.choropleth_mapbox(wifi_hotspots, geojson=bogota_geojson, color=map_option,
                               locations="localidad", featureidkey="properties.Nombre de la localidad",
                               color_continuous_scale=px.colors.sequential.Inferno,
                               center={"lat": 4.3000000, "lon": -74.2000000},
                               mapbox_style="carto-positron", zoom=8,
                               opacity=0.5)

    fig.add_scattermapbox(lat=bogota_malls["longitude"],
                          lon=bogota_malls["latitude"],
                          marker=dict(
                              size=12, color='rgb(235, 0, 100)')  # , opacity=0),
                          #marker_line=dict(width=2, color='DarkSlateGrey')
                          )

    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
