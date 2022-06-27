import dash
import plotly.express as px
import json
import pandas as pd
from random import randrange
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash import html

def display():
    
    layout = html.Div(
        [
            html.H4(["Crimenes por localidad"]),
            html.Div([
                dcc.Graph(figure=figura())
            ])
            
        ],id="crime_map"
    )
    return layout

def figura():
        
    sel_grp = pd.read_csv("./data-cleaned/Delitos_x_localidad.csv")
    with open("./data-cleaned/poligonos-localidades-min.json") as response:
        loc = json.load(response)
    fig = px.choropleth_mapbox(sel_grp, geojson=loc, color="Delito",
                               locations="Localidad", featureidkey="properties.Nombre de la localidad",
                               color_discrete_sequence=['blue'],
                               center={"lat": 4.5500000, "lon": -74.1000000},
                               mapbox_style="carto-positron", zoom=9)
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig

crime_map = display()

# map_crime = html.Div([
#     dcc.Graph(id="choropleth-map"),
#     dcc.Checklist(id='type',
#                   options=[{'label': str(b), 'value': b}
#                            for b in sorted(df['type'].unique())],
#                   value=[b for b in sorted(df['type'].unique())],
#                   inline=True,
#                   labelStyle={"margin": "1rem 1rem 0 0"},
#                   inputStyle={"margin-right": "0.25rem"}
#                   ),

# ], style=MARGIN_TOP)