from logging import exception
import os
import pickle
import numpy as np
import pandas as pd

def use_model(poll=list(), model_name='model6.pkl'):
    """
    This module is for charge a model (kmenas) and process a list of data to identify in which group 
    is the information associated in the list. This module is an specific module so it not construct
    for general purposes.
    """

    # Found the folder that contains the models and obtain all the files that are inside.
    current_dir = os.getcwd()
    model_dir = os.path.join(current_dir, 'model')
    basicdf_dir = os.path.join(current_dir, 'data-cleaned')
    model_list = [os.path.join(model_dir, item) for item in os.listdir(model_dir)]

    # Charge the model that was selected 
    try: 
        for model_path in model_list:
            if model_path.find(model_name) > 0:
                model = pickle.load(open(model_path, "rb"))
    except ValueError:
        print("The model " + model_name + ' is not found in the model folder.') 

    # Charge the template of the df to obtain X
    X = pd.read_csv(basicdf_dir + '/Plantilla.csv')

    # Variables used to organize the X
    numeric_questions = [['GASTO EN DOLARES_norm', 0, 60000], 
                       ['¿CUANTAS NOCHES DURMIO EN BOGOTA?_norm', 0, 730], 
                       ['CUANTAS VECES VISITO BOGOTA EN EL ULTIMO AÑO_norm', 0, 365], 
                       ['¿CON CUANTAS PERSONAS VIAJA?_norm', 0, 50], 
                       ['MENORES DE EDAD_norm', 0, 25]]
    categorical_questions = ['MOTIVO PRINCIPAL', 
                            'OCUPACION ACTUAL', 
                            'LUGAR DE RESIDENCIA', 
                            'NACIONALIDAD COLOMBIANA', 
                            'SEXO', 
                            'EDAD', 
                            '¿CON QUIEN VIAJA?', 
                            'NIVEL EDUCATIVO', 
                            'PRIMERA VISITA', 
                            'ALOJAMIENTO']

    for value, i in zip(poll, range(15)):
        if i < 5:
            num = int(value) - numeric_questions[i][1]
            den = numeric_questions[i][2] - numeric_questions[i][1]
            X.loc[0, numeric_questions[i][0]] = num / den
        else:
            #print(categorical_questions[i-5] + '_' + value)
            X.loc[0, categorical_questions[i-5] + '_' + value] = 1
    
    return model.predict(X)[0]

if __name__ == '__main__':
    prueba1 = [0, 1, 10, 1, 0, 'NEGOCIOS Y MOTIVOS PROFESIONALES',
            'NS/NR', 'INTERNACIONAL', 'NO', 'MUJER', 'DE 31 A 45',
            'SOLO', 'NS/NR', 'NO', 'HOTEL'] # 1 5 6
    prueba2 = [801.4768547, 90, 2, 1, 0, 'EDUCACION Y FORMACION',
            'ESTUDIANTE', 'INTERNACIONAL', 'SI', 'MUJER', 'DE 18 A 30',
            'SOLO', 'ESTUDIOS DE POSGRADO', 'NO', 
            'CASA PROPIA, DE FAMILIARES O AMIGOS (SIN PAGO)'] # 	0 4 0
    prueba3 = [160.2953709, 4, 2, 2, 0, 'TRABAJO REMUNERADO EN BOGOTA', 
            'EMPLEADO', 'INTERNACIONAL', 'SI', 'HOMBRE', 'DE 31 A 45',
            'COMPAÑERO DE TRABAJO Y/O ESTUDIO', 'NS/NR', 'NO', 'HOTEL'] # 4 6 1

    soluciones = [[1, 5, 6],
                  [0, 4, 0],
                  [4, 6, 1]]

    pruebas = [prueba1, prueba2, prueba3]
    modelos = ['model5',
               'model6',
               'model7']

    for prueba, solucion, i in zip(pruebas, soluciones, range(3)):
        print('prueba' + str(i))
        for modelo, sol in zip(modelos, solucion):
            pred = use_model(poll=prueba, model_name=modelo)
            print('Predicción: ' + str(pred) + '. Resultado: ' + str(sol))

