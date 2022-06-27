from dash import Dash, dcc, html, Input, Output, ALL
import pandas as pd
import plotly.express as px
import json
import dash_bootstrap_components as dbc

# Components
from components.content import content
from components.content import main_view
from components.sidebar import sidebar
from components.jumbotron import jumbotron

# Pages
from pages.tourist_form import radios_input
from pages.perfiles import cards


app = Dash(__name__,
           external_stylesheets=[
               dbc.themes.LUX], suppress_callback_exceptions=True,
           meta_tags=[{"name": "viewport",
                       "content": "width=device-width, initial-scale=1"}]
           )

app.title = "Turismo Bogotá"
token = "pk.eyJ1Ijoiam9yY2hlY2x1bmllIiwiYSI6ImNsNHRiOWQzZDE5YmkzamxwM2k2YTZiNGUifQ.a8403FjDkiW0wAO_bO4lLg"

server = app.server

# Load data
df = pd.read_csv("./data-cleaned/scattermap_points.csv")
# TODO: arreglar municipios aledanos
localidades_df = pd.read_csv("./data-cleaned/localidades_properties.csv")
with open("./data-cleaned/poligonos-localidades-min.json") as response:
    bogota_geojson = json.load(response)
crime = pd.read_csv("./data-cleaned/Delitos_x_localidad.csv")

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


# Build interactive map
@app.callback(
    [Output("choropleth-map", "figure"),
     Output("kpi_crime", "children"),
     Output("kpi_mean_hotel_price", "children"),
     Output("kpi_number_of_touristic_attractions", "children")],
    [Input("localidad", "value"),
     Input("type", "value"),
     Input("all_localidades_checkbox", "value")])
def display_map(chosen_localidades, chosen_type, show_all_localidades):
    # Default KPI's when seeing the entire bogota map figure.
    kpi_crime = "4500 delitos reportados en Bogotá"
    kpi_mean_hotel_price = "$8043 precio promedio en Bogotá"
    kpi_number_of_touristic_attractions = "3289 atractivos turisticos en Bogotá"

    # Default values when the user is seeing the entire bogota map figure.
    map_zoom = 9
    map_center = {"lat": 4.5500000, "lon": -74.1000000}
    marker_size = 6

    # Handle map if user hasn't selected a specific localidad.
    all_localidades = [b for b in sorted(df['localidad'].unique())]
    if (show_all_localidades == ["on"]):
        chosen_localidades = all_localidades
    elif (show_all_localidades != ["on"] and chosen_localidades != None):
        # When there's a specific localidad selected, we adjust the center and the zoom values.
        chosen_localidad_props = localidades_df[localidades_df['name']
                                                == chosen_localidades]
        map_zoom = chosen_localidad_props['zoom'].item()
        chosen_localidad_center = pd.eval(
            chosen_localidad_props['center_coordinates'].item())
        map_center = {"lat": chosen_localidad_center[0],
                      "lon": chosen_localidad_center[1]}
        marker_size = 10
        chosen_localidades = [chosen_localidades]

        # We also display the specific KPI's for the selected localidad.
        kpi_crime = "{} delitos reportados en {}".format(
            chosen_localidad_props['kpi_crime'].item(), chosen_localidad_props['name'].item())
        kpi_number_of_touristic_attractions = "{} atractivos turisticos en {}".format(
            chosen_localidad_props['number_of_touristic_attractions'].item(), chosen_localidad_props['name'].item())
        # TODO: add KPI for mean hotel value once we have it.
    else:
        chosen_localidades = [chosen_localidades]

    # Filter the dataframe to the selected localidad and scatter points.
    filtered_df = df[(df['localidad'].isin(chosen_localidades))
                     & (df['type'].isin(chosen_type))]

    # Choropleth map exactly how you would do it on a jupyter notebook.
    fig = px.choropleth_mapbox(filtered_df, geojson=bogota_geojson, color="localidad",
                               locations="localidad", featureidkey="properties.Nombre de la localidad",
                               color_discrete_sequence=['red'],
                               center=map_center,
                               zoom=map_zoom,
                               opacity=0.1)

    fig.add_scattermapbox(lat=filtered_df['latitude'],
                          lon=filtered_df['longitude'],
                          marker=dict(size=marker_size,
                                      color=filtered_df['color']),
                          hovertemplate=filtered_df['type'] +
                          ": " + filtered_df['name']
                          )

    fig.update_layout(mapbox_style="streets",
                      mapbox_accesstoken=token)
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig.update_layout(uirevision='foo')
    fig.update_layout(showlegend=False)
    return fig, kpi_crime, kpi_mean_hotel_price, kpi_number_of_touristic_attractions


@app.callback(Output("localidad", "style"), [Input("all_localidades_checkbox", "value")])
def hide_dropdown(show_all_localidades):
    """
    Shows or hide localidades dropdown depending on the checkbox to show all
    localidades.
    """
    if (show_all_localidades == ["on"]):
        return {"display": "none"}
    else:
        return {"display": "block"}


@app.callback(
    Output("radioitems-checklist-output", "children"),
    [Input({'type': 'my-numeric-input', 'index': ALL}, 'value'),
     Input({'type': 'my-radio-input', 'index': ALL}, 'value')],
)
def on_form_change(numerical_input_values, radio_button_values):
    """
    Handles form values being changed and validated to pass onto the model.
    """
    for (i, value) in enumerate(numerical_input_values):
        print(value)
    for (i, value) in enumerate(radio_button_values):
        print(value)

    return ""


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    """
    Display different content based on the url
    """
    if pathname == "/":
        return main_view
    elif pathname == "/tu-perfil":
        return radios_input
    elif pathname == "/delincuencia":
        return html.P("Acá puede ir información y KPI's sobre delincuencia")
    elif pathname == "/sobre-nosotros":
        # html.P("Acá van los componentes de tarjeta de perfil con foto y bio de cada integrante")
        return html.Div(cards)
    # If the user tries to reach a different page, return a 404 message
    return jumbotron


if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
