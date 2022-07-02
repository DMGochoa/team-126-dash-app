import dash
import plotly.express as px
import json
import pandas as pd
from random import randrange
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash import html
from operator import xor

def display():
    
    layout = html.Div(
        [
            html.H4(["Crimenes por localidad"]),
            html.P(["La información recopilada para el análisis de los crimenes comprende los años 2021 y 2022 para la ciudad de Bogotá y fue exportada del portal de la ",html.A("Secretaria Distrital de Seguridad, Convivencia y Justicia",href="https://scj.gov.co/es/oficina-oaiee/estadisticas-mapas", target="_blank") , " en la consulta Delitos de alto impacto"]),
            html.Div([
                dcc.Graph(figure=figura())
            ]),
            html.Div([
                dcc.Graph(figure=barras())
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
                               color_continuous_scale="reds",
                               mapbox_style="carto-positron", zoom=9)
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig

def barras():
        
    df_delitos = pd.read_csv("./data/Siedco_Datos_Detallados_Delitos.csv", sep=",")
    df_delitos['Localidad']=df_delitos.Localidad.str[4:]
    del_loc = df_delitos.groupby(['Localidad', 'Rango del Dia']).size().reset_index(name='Count')
    del_loc['Localidad'] = del_loc['Localidad'].str.strip()
    del_loc = del_loc[~ xor(del_loc['Localidad'] == 'SIN LOCALIZACION',del_loc['Localidad'] == 'SUMAPAZ')]
    del_loc['Rango del Dia'] = pd.Categorical(del_loc['Rango del Dia'], ["MAÑANA", "TARDE", "NOCHE", "MADRUGADA"])
    del_loc.sort_values("Rango del Dia", inplace=True)
    fig = px.bar(del_loc, x="Localidad", y="Count", color="Rango del Dia", title="Delitos por Localidad segun el rango horario",  color_discrete_map={"MAÑANA": "#FBE426", "MADRUGADA": "#0D2A63", "NOCHE": "#1616A7","TARDE": "#DC3912"})
    return fig

crime_map = display()
