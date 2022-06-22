from dash import Dash, dcc, html, Input, Output
from urllib.request import urlopen
import pandas as pd
import plotly.express as px
import json
import plotly.graph_objects as go

app = Dash(__name__)

server = app.server

# Load data
df = pd.read_csv("./data-cleaned/scattermap_points.csv")
with open("./data-cleaned/poligonos-localidades-min.json") as response:
    bogota_geojson = json.load(response)


app.layout = html.Div([
    html.H4('Bogotá'),
    html.P("Selecciona una de las opciones:"),
    dcc.Checklist(id='localidad',
                  options=[{'label': str(b), 'value': b}
                           for b in sorted(df['localidad'].unique())],
                  value=[b for b in sorted(df['localidad'].unique())],
                  inline=True
                  ),
    dcc.Checklist(id='type',
                  options=[{'label': str(b), 'value': b}
                           for b in sorted(df['type'].unique())],
                  value=[b for b in sorted(df['type'].unique())],
                  inline=True
                  ),
    dcc.Graph(id="choropleth-map"),
])


@app.callback(
    Output("choropleth-map", "figure"),
    [Input("localidad", "value"),
     Input("type", "value")])
def display_choropleth(chosen_localidad, chosen_type):
    filtered_df = df[(df['localidad'].isin(chosen_localidad))
                     & (df['type'].isin(chosen_type))]

    # Map choropleth map exactly how you would do it on a jupyter notebook
    fig = px.choropleth_mapbox(filtered_df, geojson=bogota_geojson, color="localidad",
                               locations="localidad", featureidkey="properties.Nombre de la localidad",
                               color_discrete_sequence=['blue'],
                               center={"lat": 4.5500000, "lon": -74.1000000},
                               mapbox_style="carto-positron", zoom=9,
                               opacity=0.1)

    fig.add_scattermapbox(lat=filtered_df['latitude'],
                          lon=filtered_df['longitude'],
                          marker=dict(color=filtered_df['color']),
                          hovertext=filtered_df['localidad']
                          )

    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig.update_layout(uirevision='foo')
    fig.update_layout(showlegend=False)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
