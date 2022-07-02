from pydoc import visiblename
from re import M
import plotly.express as px
import json
import pandas as pd
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash import html
from operator import xor


def display():
    layout = dbc.Container(
        [
            dbc.Row([
                dbc.Col(
                    html.Div([
                        html.Div([
                            html.H4("🚨️ Crimenes por localidad"),
                            html.P(
                                "Explora las localidades con más número de delitos."),
                        ], className="crime-graph-info rounded"),
                        html.Div([
                            html.P(["🗣️️ Fuente: la información recopilada para el análisis de los crimenes comprende los años 2021 y 2022 para la ciudad de Bogotá y fue exportada del portal de la ",
                                    html.A(
                                        "Secretaria Distrital de Seguridad, Convivencia y Justicia", href="https://scj.gov.co/es/oficina-oaiee/estadisticas-mapas", target="_blank"), " en la consulta Delitos de alto impacto."]),
                        ], style={"padding": "1rem"}),
                    ]), md="4"),
                dbc.Col(dcc.Graph(figure=figura()), md="8"),
            ], style={"marginBottom": "2rem"}),
            html.Hr(),
            dbc.Row([
                html.Div([
                    html.H4(["🕒 Crimen por rango de horas"]),
                    html.P(
                        "Explora las localidades con mayor crimen y cuando estos crimenes ocurren durante el día 🌅🌇🌌")
                ], className="crime-graph-info crime-by-time-of-day rounded"),
                dbc.Col(dcc.Graph(figure=barras())),
            ], style={"marginTop": "2rem"}),
        ], id="crime_map"
    )
    return layout


def figura():
    sel_grp = pd.read_csv(
        "./data-cleaned/Delitos_x_localidad.csv", encoding='utf8')
    with open("./data-cleaned/poligonos-localidades-min.json") as response:
        loc = json.load(response)
    fig = px.choropleth_mapbox(sel_grp, geojson=loc, color="Delitos",
                               locations="Localidad", featureidkey="properties.Nombre de la localidad",
                               color_discrete_sequence=['blue'],
                               center={"lat": 4.5500000, "lon": -74.1000000},
                               color_continuous_scale="reds",
                               mapbox_style="carto-positron", zoom=9)
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig


def barras():
    df_delitos = pd.read_csv(
        "./data/Siedco_Datos_Detallados_Delitos.csv", sep=",")
    df_delitos['Localidad'] = df_delitos.Localidad.str[4:]
    del_loc = df_delitos.groupby(
        ['Localidad', 'Rango del Dia']).size().reset_index(name='Count')
    del_loc['Localidad'] = del_loc['Localidad'].str.strip()
    del_loc = del_loc[~ xor(
        del_loc['Localidad'] == 'SIN LOCALIZACION', del_loc['Localidad'] == 'SUMAPAZ')]
    del_loc['Rango del Dia'] = pd.Categorical(
        del_loc['Rango del Dia'], ["MAÑANA", "TARDE", "NOCHE", "MADRUGADA"])
    del_loc.sort_values("Rango del Dia", inplace=True)
    # Colors from: https://www.color-hex.com/color-palette/14359
    fig = px.bar(del_loc, x="Localidad", y="Count", color="Rango del Dia", labels={
        "Count": "Delitos",
        "Localidad": "",
        "Rango del Dia": "",
    }, color_discrete_map={"MAÑANA": "#e8817f", "MADRUGADA": "#311f62", "NOCHE": "#5a336e", "TARDE": "#8d5273"})

    fig.update_layout(margin={"r": 0, "t": 25, "l": 0, "b": 0})
    return fig


crime_map = display()
