import dash_bootstrap_components as dbc
from dash import html

# https://drive.google.com/uc?export=view&id=1nDjXooBHQpB8aR4sHg5iMQYU-2MKRCwC
andresCuellar = {
    'foto': './assets/img/Andres_Cuellar.jpeg',
    'nombre': 'Andres Cuellar',
    'descripcion': 'Después de tratar por dos años seguidos de entrar a DS4A por fin',
    'contacto': 'andrescuellar@team126.com'
}
# https://drive.google.com/uc?export=view&id=1bTIqtTg7wQ6rPs-ba5TDV93Sk0kzjx9_
albertoRamirez = {
    'foto': './assets/img/Alberto_Ramirez.jpeg',
    'nombre': 'Alberto Ramirez',
    'descripcion': 'Ingeniero de sistemas con especializaciones en analítica de la Universidad Nacional y sistemas de información de la Universidad Eafit, especialista en ingeligencia de negocios en Holcim NA',
    'contacto': 'alvertorave@gmail.com - in/albertoramirez2'
}

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
    'descripcion': 'Después de tratar por dos años seguidos de entrar a DS4A por fin',
    'contacto': 'juandiaz@team126.com'
}
# https://drive.google.com/uc?export=view&id=1PTvtwqMo7FLd4K-78mvVPvKneBY0rubH
juanHurtado = {
    'foto': './assets/img/Juan_Hurtado.jpeg',
    'nombre': 'Juan Fernando Hurtado',
    'descripcion': 'Ingeniero electrónico',
    'contacto': 'juanf.hurtadov@gmail.com'
}

diegoMoreno = {
    'foto': 'Diego_Moreno.jpeg',
    'nombre': 'Diego Alejandro Moreno',
    'descripcion': 'Ingeniero eléctrico con un gran interés en IA, próximamente estará ingresando a la maestría en ingeniería eléctrica con un enfoque en gestión y automatización.',
    'contacto': 'diegomore1997@gmail.com' + ' ' + 'https://www.linkedin.com/in/diegoamg/'
}


def card_perfil(foto, nombre, descripcion, contacto):
    card = dbc.Card(
        [
            dbc.Row(
                [
                    dbc.Col(
                        dbc.CardImg(
                            src=foto,
                            className="img-fluid rounded-start",
                        ),
                        className="col-md-4",
                    ),
                    dbc.Col(
                        dbc.CardBody(
                            [
                                html.H4(nombre, className="card-title"),
                                html.P(descripcion,
                                       className="card-text",
                                       ),
                                html.Small(contacto,
                                           className="card-text text-muted",
                                           ),
                            ]
                        ),
                        className="col-md-8",
                    ),
                ],
                className="g-0 d-flex align-items-center",
            )
        ],
        className="mb-3",
        style={"maxWidth": "540px"},
    )
    return card

row_0 = dbc.Row([
        html.H1(
            'Team 126',
            style={"font-family":"Rockwell",
                   "text-align":"center"}
        ),
        html.H2(
            'DS4A',
            style={"font-family":"Rockwell",
                   "text-align":"center"}
        )
    ]
)
row_1 = dbc.Row(
    [
        dbc.Col(dbc.Card(card_perfil(**andresCuellar),
                color="primary", outline=True)),
        dbc.Col(dbc.Card(card_perfil(**albertoRamirez),
                color="primary", outline=True)),
    ],
    className="mb-4",
)

row_2 = dbc.Row(
    [
        dbc.Col(dbc.Card(card_perfil(**carmenDelgado),
                color="primary", outline=True)),
        dbc.Col(dbc.Card(card_perfil(**juanDiaz),
                color="primary", outline=True)),
    ],
    className="mb-4",
)

row_3 = dbc.Row(
    [
        dbc.Col(dbc.Card(card_perfil(**juanHurtado), color="primary", outline=True)),
        dbc.Col(dbc.Card(card_perfil(**diegoMoreno),
                color="primary", outline=True)),
    ],
    className="mb-4",
)

RB=[
    {
    "autoria":"puede ser un autor individual, colectivo (grupo de personas) o una organización",
    "fecha":"año de publicación del dataset o fecha en que fue accesible online",
    "titulo":"denominación del dataset",
    "edicion":"etapa del procesamiento de datos, indicando si son datos en bruto o refinados",
    "version":"aumenta de número según cambian los datos, fruto de revisiones y actualizaciones",
    "editor":"entidad responsable de producir y/o distribuir el dataset. El productor es la organización que patrocina la investigación; y el distribuidor es la organización que da accesibilidad al dataset para su descarga y uso.",
    "tipo_de_recurso":"“database”, “dataset”",
    "ubicacion":"URL persistente que permita acceder al conjunto o subconjunto de datos (DOI, Handle …)",
    },
]
def refBiblio(posicion):
    referencia=""
    for key in RB[posicion]:
        referencia=referencia+" "+RB[posicion][key]
    referencia=referencia.strip()
    return referencia

row_4=dbc.Row([
    html.H3(
            'Referencias bibliográficas',
            style={"font-family":"Arial",
                   "text-align":"left"}
        ),
    html.P(
        refBiblio(0),
        style={"text-align":"justify"}   
    )
]
              
    
    
)

cards = html.Div([row_0,row_1, row_2, row_3,row_4]) #html.Div([row_0,row_1, row_2, row_3],row_4)
