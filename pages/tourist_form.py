from dash import dcc, html
import dash_bootstrap_components as dbc


def create_radio_options(possible_options):
    """
    Helper function to create the options array of dictionary objects following
    the Dash components standard for radio buttons.
    """
    options = []
    for option in possible_options:
        options.append({"label": option, "value": option})

    return options


NUMERICAL_INPUT_QUESTIONS = [{
    "id": "numerical-range-question-1",
    "question": "¿Cuánto piensa gastar (en dólares)?",
    "min": 0,
    "max": 60000
}, {
    "id": "numerical-range-question-2",
    "question": "¿Cuántas noches piensa dormir en Bogotá?",
    "min": 0,
    "max": 730
}, {
    "id": "numerical-range-question-3",
    "question": "¿Cuántas veces visitó Bogotá en el último año?",
    "min": 0,
    "max": 365
}, {
    "id": "numerical-range-question-4",
    "question": "¿Con cuántas personas viaja?",
    "min": 0,
    "max": 50
}, {
    "id": "numerical-range-question-5",
    "question": "¿Con cuántos menores de edad viaja?",
    "min": 0,
    "max": 25
}]

SINGLE_CHOICE_QUESTIONS = [{
    "id": "single-choice-question-1",
    "question": "¿Cuál es el motivo principal?",
    "options": create_radio_options([
        'NEGOCIOS Y MOTIVOS PROFESIONALES',
        'VACACIONES/RECREACION/OCIO',
        'EDUCACION Y FORMACION',
        'SALUD Y ATENCION MEDICA',
        'VISITA A FAMILIARES Y AMIGOS',
        'TRABAJO REMUNERADO EN BOGOTA',
        'OTRO MOTIVO',
        'COMPRAS',
        'RELIGION/PEREGRINACIONES'
    ]),
}, {
    "id": "single-choice-question-2",
    "question": "¿Ocupación actual?",
    "options": create_radio_options([
        'EMPLEADO',
        'ESTUDIANTE',
        'OFICIOS DEL HOGAR',
        'RENTISTA Y/O PENSIONADO',
        'TRABAJADOR INDEPENDIENTE',
        'OTRO',
        'PATRON O EMPLEADOR',
        'DESEMPLEADO'
    ]),
}, {
    "id": "single-choice-question-3",
    "question": "¿Lugar de residencia?",
    "options": create_radio_options([
        'INTERNACIONAL',
        'NACIONAL',
    ]),
}, {
    "id": "single-choice-question-4",
    "question": "Sexo",
    "options": create_radio_options([
        'MUJER',
        'HOMBRE',
        'NS/NR'
    ]),
}, {
    "id": "single-choice-question-5",
    "question": "¿En qué rango de edad está?",
    "options": create_radio_options([
        'MENOR DE 18',
        'DE 18 A 30',
        'DE 31 A 45',
        'DE 46 A 60',
        'MAYOR A 60',
    ]),
}, {
    "id": "single-choice-question-6",
    "question": "¿Con quién viaja?",
    "options": create_radio_options([
        'SOLO',
        'FAMILIA',
        'COMPAÑERO DE TRABAJO Y/O ESTUDIO',
        'AMIGOS',
        'PAREJA',
        'OTRO',
    ]),
}, {
    "id": "single-choice-question-7",
    "question": "¿Cuál es su nivel educativo?",
    "options": create_radio_options([
        'PROFESIONAL',
        'ESTUDIOS DE POSGRADO',
        'SECUNDARIA',
        'TECNICO O TECNOLOGICO',
        'NINGUNO',
        'PRIMARIA',
    ]),
}, {
    "id": "single-choice-question-8",
    "question": "¿Es su primera visita a Bogotá?",
    "options": create_radio_options([
        'SI',
        'NO',
    ]),

}, {
    "id": "single-choice-question-9",
    "question": "¿En dónde piensa alojarse? ",
    "options": create_radio_options([
        'HOTEL',
        'CASA PROPIA, DE FAMILIARES O AMIGOS (SIN PAGO)',
        'OTRO',
        'INMUEBLE DE ALQUILER AIRBNB',
        'HOSTAL',
        'APARTAHOTEL',
        'INMUEBLE DE ALQUILER (PAGOS POR PLATAFORMA DIG)',
    ]),
}]


def custom_radio_input(id, question, options):
    return html.Div(
        [
            dbc.Label(question, width=2),
            dbc.Col(
                dbc.RadioItems(
                    id={
                        'type': 'my-radio-input',
                        'index': id

                    },
                    options=options,
                    value=False
                ),
                width=10,
            ),
        ],
        className="mb-3",
    )


def custom_numerical_input(id, question, min, max):
    return html.Div(
        [
            dbc.Label(question, width=2),
            dbc.Col([
                dbc.Input(type="number", id={
                    'type': 'my-numeric-input',
                    'index': id
                }, min=min, max=max),
                dbc.FormText(
                    "Valor debe estar entre {} y {}".format(min, max))
            ],
                width=5,
            ),
        ],
        className="mb-3",
    )


questions = []

for item in NUMERICAL_INPUT_QUESTIONS:
    questions.append(custom_numerical_input(
        item['id'], item['question'], item['min'], item['max']))

for item in SINGLE_CHOICE_QUESTIONS:
    questions.append(custom_radio_input(
        item['id'], item['question'], item['options']))


questions.append(
    dbc.Col(dbc.Button("Enviar", color="primary", disabled=True), width="auto"))
questions.append(html.P(id="radioitems-checklist-output"))

radios_input = html.Form(questions)
