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
            html.P(["La información recopilada para el análisis de los crimenes comprende los años 2021 y 2022 para la ciudad de Bogotá y fue exportada del portal de la ",html.A("Secretaria Distrital de Seguridad, Convivencia y Justicia",href="https://scj.gov.co/es/oficina-oaiee/estadisticas-mapas", target="_blank") , " en la consulta Delitos de alto impacto"]),
            html.Div([
                dcc.Graph(figure=figura())
            ])
            
        ],id="crime_map"
    )
    return layout

def figura():
        
    sel_grp = pd.read_csv("./data-cleaned/Delitos_x_localidad.csv", encoding='utf8')
    with open("./data-cleaned/poligonos-localidades-min.json") as response:
        loc = json.load(response)
    fig = px.choropleth_mapbox(sel_grp, geojson=loc, color="Delitos",
                               locations="Localidad", featureidkey="properties.Nombre de la localidad",
                               color_discrete_sequence=['blue'],
                               center={"lat": 4.5500000, "lon": -74.1000000},
                               mapbox_style="carto-positron", zoom=9)
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig

crime_map = display()
