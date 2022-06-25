from tkinter import SINGLE
from dash import html
import dash_bootstrap_components as dbc

SINGLE_CHOICE_QUESTIONS = [{
    "id": 1,
    "question": "¿Cuál es el motivo principal?",
    "options": [
        {"label": 'NEGOCIOS Y MOTIVOS PROFESIONALES', "value": 0},
        {"label": 'VACACIONES/RECREACION/OCIO', "value": 1},
        {"label": 'EDUCACION Y FORMACION', "value": 2},
        {"label": 'SALUD Y ATENCION MEDICA', "value": 3},
        {"label": 'VISITA A FAMILIARES Y AMIGOS', "value": 4},
        {"label": 'TRABAJO REMUNERADO EN BOGOTA', "value": 5},
        {"label": 'NS/NR', "value": 6},
        {"label": 'OTRO MOTIVO', "value": 7},
        {"label": 'COMPRAS', "value": 8},
        {"label": 'RELIGION/PEREGRINACIONES', "value": 9}],
}, {
    "id": 2,
    "question": "¿Ocupación actual?",
    "options": [{"label": 'NS/NR', "value": 10},
                {"label": 'EMPLEADO' 'ESTUDIANTE', "value": 11},
                {"label": 'OFICIOS DEL HOGAR', "value": 12},
                {"label": 'RENTISTA Y/O PENSIONADO', "value": 13},
                {"label": 'TRABAJADOR INDEPENDIENTE', "value": 14},
                {"label": 'OTRO', "value": 15},
                {"label": 'PATRON O EMPLEADOR', "value": 16},
                {"label": 'DESEMPLEADO', "value": 17}]
}]


def custom_radio_input(label, options):
    return html.Div(
        [
            dbc.Label(label, html_for="example-radios-row", width=2),
            dbc.Col(
                dbc.RadioItems(
                    id="example-radios-row",
                    options=options,
                ),
                width=10,
            ),
        ],
        className="mb-3",
    )


questions = []

for item in SINGLE_CHOICE_QUESTIONS:
    questions.append(custom_radio_input(item['question'], item['options']))


questions.append(dbc.Col(dbc.Button("Submit", color="primary"), width="auto"))

radios_input = html.Div(questions)
