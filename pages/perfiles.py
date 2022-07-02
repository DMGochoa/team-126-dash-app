import dash_bootstrap_components as dbc
from dash import html

team_members = [
    {
        'foto': './assets/img/Andres_Cuellar.jpeg',
        'nombre': 'Andres Cuellar',
        'descripcion': 'Ingeniero de sistemas. Software engineer @ Uber. Apasionado por aprender.',
        'linkedin_url': 'https://www.linkedin.com/in/andrescuco/'
    },
    {
        'foto': './assets/img/Alberto_Ramirez.jpeg',
        'nombre': 'Alberto Ramirez',
        'descripcion': 'Ingeniero de sistemas con especializaciones en analítica de la Universidad Nacional y sistemas de información de la Universidad Eafit, especialista en inteligencia de negocios en Holcim NA',
        'linkedin_url': 'https://www.linkedin.com/in/albertoramirez2/'
    },
    {
        'foto': './assets/img/placeholder-image.png',
        'nombre': 'Carmen Delgado',
        'descripcion': 'Después de tratar por dos años seguidos de entrar a DS4A por fin',
        'linkedin_url': 'https://www.linkedin.com/in/andrescuco/'
    },
    {
        'foto': './assets/img/Juan_Felipe_Diaz.jpg',
        'nombre': 'Juan Felipe Diaz',
        'descripcion': 'Estudiante de ultimos semestres de ingeniería con interés de conocer de la ciencia y analítica de datos.',
        'linkedin_url': 'https://www.linkedin.com/in/juanfelipediazr/'
    },
    {
        'foto': './assets/img/Juan_Hurtado.jpeg',
        'nombre': 'Juan Fernando Hurtado',
        'descripcion': 'Ingeniero electrónico',
        'linkedin_url': 'https://www.linkedin.com/in/andrescuco/'
    },
    {
        'foto': './assets/img/placeholder-image.png',
        'nombre': 'Diego Alejandro Moreno',
        'descripcion': 'Ingeniero eléctrico con un gran interés en IA, próximamente estará ingresando a la maestría en ingeniería eléctrica con un enfoque en gestión y automatización.',
        'linkedin_url': 'https://www.linkedin.com/in/diegoamg/'
    },
]

carmenDelgado = {
    'foto': 'Carmen_Delgado.jpeg',
    'nombre': 'Carmen Delgado',
    'descripcion': 'Después de tratar por dos años seguidos de entrar a DS4A por fin',
    'contacto': 'carmendelgado@team126.com'
}
# https://drive.google.com/uc?export=view&id=1wUyL20fsmTTmlQjGWIMp7sD3bGBX4p-F
juanDiaz = {
    'foto': './assets/img/Juan_Felipe_Diaz.jpg',
    'nombre': 'Juan Felipe Diaz',
    'descripcion': 'Estudiante de ultimos semestres de ingeniería con interés de conocer de la ciencia y analítica de datos.',
    'contacto': 'diazrochajuanfe@yahoo.com.mx - in/juanfelipediazr'
}
# https://drive.google.com/uc?export=view&id=1PTvtwqMo7FLd4K-78mvVPvKneBY0rubH
juanHurtado = {
    'foto': './assets/img/Juan_Hurtado.jpeg',
    'nombre': 'Juan Fernando Hurtado',
    'descripcion': 'Ingeniero electrónico',
    'contacto': 'juanf.hurtadov@gmail.com'
}
#https://drive.google.com/file/d/1MzqpS21klr225yWk0YgZ6wPgibIEcUE6/view?usp=sharing
diegoMoreno = {
    'foto': './assets/img/Diego_Moreno.jpg',
    'nombre': 'Diego Alejandro Moreno',
    'descripcion': 'Ingeniero eléctrico con un gran interés en IA, próximamente estará ingresando a la maestría en ingeniería eléctrica con un enfoque en gestión y automatización.',
    'contacto': 'diegomore1997@gmail.com' + ' ' + 'https://www.linkedin.com/in/diegoamg/'
}

RB = [
    {
        "autoria": "Infraestructura de datos espaciales de Bogotá - IDECA,",
        "fecha": "15-08-2017,",
        "titulo": "poligonos-localidades,",
        "edicion": "datos refinados,",
        "version": "",
        "editor": "Infraestructura de datos espaciales de Bogotá - IDECA,",
        "tipo_de_recurso": "“database”, “dataset,”",
        "ubicacion": "https://datosabiertos.bogota.gov.co/dataset/localidad-bogota-d-c",
    },
    {
        "autoria": "Instituto Distrital de Turismo,",
        "fecha": "31-12-2019,",
        "titulo": "Inventario Turístico,",
        "edicion": "datos refinados,",
        "version": "",
        "editor": "Instituto Distrital de Turismo,",
        "tipo_de_recurso": "“database”, “dataset,”",
        "ubicacion": "https://www.ideca.gov.co/recursos/mapas/inventario-turistico",
    },
    {
        "autoria": "Alta Consejería Distrital de TIC,",
        "fecha": "08-11-2019,",
        "titulo": "Zonas Wifi gratis. Bogotá D.C.,",
        "edicion": "datos refinados,",
        "version": "",
        "editor": "Alta Consejería Distrital de TIC,",
        "tipo_de_recurso": "“database”, “dataset,”",
        "ubicacion": "https://www.ideca.gov.co/recursos/mapas/zonas-wifi-gratis-bogota-dc",
    },
    {
        "autoria": "Empresa Transporte Tercer Milenio,",
        "fecha": "23-04-2019,",
        "titulo": "Paradero SITP. Bogotá D.C,",
        "edicion": "datos refinados,",
        "version": "",
        "editor": "Empresa Transporte Tercer Milenio,",
        "tipo_de_recurso": "“database”, “dataset,”",
        "ubicacion": "https://www.ideca.gov.co/recursos/mapas/paradero-sitp-bogota-dc-0",
    },
    {
        "autoria": "Empresa Transporte Tercer Milenio,",
        "fecha": "13-05-2021,",
        "titulo": "Estación de Transmilenio para Bogotá D.C.,",
        "edicion": "datos refinados,",
        "version": "",
        "editor": "Empresa Transporte Tercer Milenio,",
        "tipo_de_recurso": "“database”, “dataset,”",
        "ubicacion": "https://www.ideca.gov.co/recursos/mapas/estacion-de-transmilenio-para-bogota-dc",
    },
    {
        "autoria": "Secretaría Distrital de Seguridad, Convivencia y Justicia,",
        "fecha": "13-06-2022,",
        "titulo": "Delito de Alto Impacto. Bogotá D.C.,",
        "edicion": "datos refinados,",
        "version": "",
        "editor": "Secretaría Distrital de Seguridad, Convivencia y Justicia,",
        "tipo_de_recurso": "“database”, “dataset,”",
        "ubicacion": "https://datosabiertos.bogota.gov.co/dataset/delito-de-alto-impacto-bogota-d-c",
    },
    {
        "autoria": "Instituto Para La Economía Social – IPES,",
        "fecha": "22-10-2020,",
        "titulo": "Centros comerciales 2020,",
        "edicion": "datos refinados,",
        "version": "",
        "editor": "Instituto Para La Economía Social – IPES,",
        "tipo_de_recurso": "“database”, “dataset,”",
        "ubicacion": "https://datosabiertos.bogota.gov.co/dataset/centros-comerciales/resource/8efe71cb-fb12-4d63-a449-6fc06fbde27b",
    },
    {
        "autoria": "Instituto distrital de turismo,",
        "fecha": "09-06-2022,",
        "titulo": "Viajeros,",
        "edicion": "datos refinados,",
        "version": "",
        "editor": "Instituto distrital de turismo,",
        "tipo_de_recurso": "“database”, “dataset,”",
        "ubicacion": "",
    },
    {
        "autoria": "Instituto distrital de turismo,",
        "fecha": "01-06-2022,",
        "titulo": "precio hotel,",
        "edicion": "datos refinados,",
        "version": "",
        "editor": "Instituto distrital de turismo,",
        "tipo_de_recurso": "“database”, “dataset,”",
        "ubicacion": "",
    },
]


def profile_card(foto, nombre, descripcion, linkedin_url):
    return dbc.Card(
        [
            dbc.Row(
                [
                    dbc.Col(
                        dbc.CardImg(
                            src=foto,
                            className="profile-card-img img-fluid rounded",
                        ),
                        className="col-md-4",
                    ),
                    dbc.Col(
                        dbc.CardBody(
                            [
                                html.H5(nombre, className="card-title"),
                                html.P(descripcion, className="card-text"),
                                html.A(html.I(className="bi bi-linkedin"),
                                       href=linkedin_url, target="__blank")
                            ]
                        ),
                        className="col-md-8",
                    ),
                ],
                className="g-0 d-flex align-items-center rounded",
            )
        ],
        className="mb-3 rounded",
        style={"maxWidth": "540px"},
    )


def build_source(posicion):
    referencia = "‣"
    for key in RB[posicion]:
        referencia = referencia+" "+RB[posicion][key]
    referencia = referencia.strip()
    return referencia


row_0 = dbc.Row([
    html.H2('🧑‍🔬 Equipo 126 — DS4A')
], className='profiles-sources-title rounded')

member_cards = []

for member in team_members:
    member_cards.append(dbc.Row(
        [
            dbc.Col(profile_card(member['foto'], member['nombre'],
                    member['descripcion'], member['linkedin_url']), className="rounded"),
        ],
    ))

references = html.Div([
    html.H4('📚 Referencias bibliográficas'),
    html.Hr(),
    html.P(build_source(0)),
    html.P(build_source(1)),
    html.P(build_source(2)),
    html.P(build_source(3)),
    html.P(build_source(4)),
    html.P(build_source(5)),
    html.P(build_source(6)),
    html.P(build_source(7)),
    html.P(build_source(8)),
], className="references-container rounded")

row_1 = dbc.Row([
    dbc.Col(member_cards, className="md-4"),
    dbc.Col(references),
], style={"marginTop": "1.5rem"})

cards = html.Div(
    [row_0, row_1])
