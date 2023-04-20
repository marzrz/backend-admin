from flask_cors import CORS
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson import json_util, ObjectId
import numpy as np
import pandas as pd

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://conversational.ugr.es:27020/bon-app-petit"
mongo = PyMongo(app)


def demtest():
    age = []
    alergia = []
    altura = []
    cereales_integrales = []
    comida_pantalla = []
    dispositivo_2h = []
    endulzante = []
    estudios_p1 = []
    estudios_p2 = []
    fruta = []
    genre = []
    habitos_saludables = []
    hermanos = []
    impulsividad = []
    intervencion = []
    laboral_p1 = []
    laboral_p2 = []
    lugar_comida = []
    peso = []
    saciado = []
    user_list = []
    user_documents = mongo.db.user.find()
    for doc in user_documents:
        user = json_util.loads(json_util.dumps(doc))
        user_list.append(user['username'])
        if user['initialized']:
            if user['dem_test_complete']:
                demtest_json = json_util.loads(json_util.dumps(user['dem_test']))
                age.append(int(demtest_json['age']))
                alergia.append(demtest_json['alergia'])
                altura.append(demtest_json['altura'])
                cereales_integrales.append(demtest_json['cereales_integrales'])
                comida_pantalla.append(demtest_json['comida_pantalla'])
                dispositivo_2h.append(demtest_json['dispositivo_2h'])
                endulzante.append(demtest_json['endulzante'])
                estudios_p1.append(demtest_json['estudios_p1'])
                estudios_p2.append(demtest_json['estudios_p2'])
                fruta.append(demtest_json['fruta'])
                genre.append(demtest_json['genre'])
                habitos_saludables.append(demtest_json['habitos_saludables'])
                hermanos.append(int(demtest_json['hermanos']))
                impulsividad.append(demtest_json['impulsividad'])
                intervencion.append(demtest_json['intervencion'])
                laboral_p1.append(demtest_json['laboral_p1'])
                laboral_p2.append(demtest_json['laboral_p2'])
                lugar_comida.append(demtest_json['lugar_comida'])
                peso.append(demtest_json['peso'])
                saciado.append(demtest_json['saciado'])
            else:
                age.append(None)
                alergia.append(None)
                altura.append(None)
                cereales_integrales.append(None)
                comida_pantalla.append(None)
                dispositivo_2h.append(None)
                endulzante.append(None)
                estudios_p1.append(None)
                estudios_p2.append(None)
                fruta.append(None)
                genre.append(None)
                habitos_saludables.append(None)
                hermanos.append(None)
                impulsividad.append(None)
                intervencion.append(None)
                laboral_p1.append(None)
                laboral_p2.append(None)
                lugar_comida.append(None)
                peso.append(None)
                saciado.append(None)
        else:
            age.append(None)
            alergia.append(None)
            altura.append(None)
            cereales_integrales.append(None)
            comida_pantalla.append(None)
            dispositivo_2h.append(None)
            endulzante.append(None)
            estudios_p1.append(None)
            estudios_p2.append(None)
            fruta.append(None)
            genre.append(None)
            habitos_saludables.append(None)
            hermanos.append(None)
            impulsividad.append(None)
            intervencion.append(None)
            laboral_p1.append(None)
            laboral_p2.append(None)
            lugar_comida.append(None)
            peso.append(None)
            saciado.append(None)

    demtest = {'age': age, 'alergia': alergia, 'altura': altura, 'cereales_integrales': cereales_integrales,
               'comida_pantalla': comida_pantalla, 'dispositivo_2h': dispositivo_2h, 'endulzante': endulzante,
               'estudios_p1': estudios_p1, 'estudios_p2': estudios_p2, 'fruta': fruta, 'genre': genre,
               'habitos_saludables': habitos_saludables, 'hermanos': hermanos, 'impulsividad': impulsividad,
               'intervencion': intervencion, 'laboral_p1': laboral_p1, 'laboral_p2': laboral_p2,
               'lugar_comida': lugar_comida, 'peso': peso, 'saciado': saciado}
    df = pd.DataFrame(demtest, index=user_list)

    return df



def kidmed():
    user_list = []
    user_documents = list(mongo.db.user.find())
    kidmed = [[None] * 17] * len(user_documents)
    for doc in user_documents:
        user = json_util.loads(json_util.dumps(doc))
        user_list.append(user['username'])
        i = 0
        if user['initialized'] and user['kidmed_complete']:
            kidmed_json = json_util.loads(json_util.dumps(user['kidmed']))
            for info in kidmed_json:
                kidmed[user_documents.index(doc)][i] = kidmed_json[info]
                i += 1
            kidmed[user_documents.index(doc)][i] = user['total_kidmed']
            i += 1


    columns = [ 'kidmed1', 'kidmed2', 'kidmed3',
               'kidmed4', 'kidmed5', 'kidmed6', 'kidmed7',
               'kidmed8', 'kidmed9', 'kidmed10', 'kidmed11',
               'kidmed12', 'kidmed13', 'kidmed14', 'kidmed15',
               'kidmed16', 'total_kidmed']

    df = pd.DataFrame(kidmed, index=user_list, columns=columns)

    print(df)

    return df


def paqc():
    user_list = []
    user_documents = list(mongo.db.user.find())
    paqc = [[None] * 39] * len(user_documents)
    for doc in user_documents:
        user = json_util.loads(json_util.dumps(doc))
        user_list.append(user['username'])
        i = 0
        if user['initialized'] and user['paqc_complete']:
            paqc_json = json_util.loads(json_util.dumps(user['paqc']))
            for info in paqc_json:
                paqcItem_json = json_util.loads(json_util.dumps(paqc_json[info]))
                if info == 'paqc_1':
                    for sport in paqcItem_json:
                        paqc[user_documents.index(doc)][i] = paqcItem_json[sport]
                        i += 1
                elif info == 'paqc_9':
                    for day in paqcItem_json:
                        paqc[user_documents.index(doc)][i] = paqcItem_json[day]
                        i += 1
                elif info == 'paqc_10':
                    for question in paqcItem_json:
                        paqc[user_documents.index(doc)][i] = paqcItem_json[question]
                        i += 1
                else:
                    paqc[user_documents.index(doc)][i] = paqcItem_json
                    i += 1



    # print(paqc)

    columns = ['paqc1_comba', 'paqc1_patinar', 'paqc1_pillapilla', 'paqc1_bicicleta',
               'paqc1_caminar', 'paqc1_correr', 'paqc1_aerobic', 'paqc1_natacion',
               'paqc1_bailar', 'paqc1_badminton', 'paqc1_rugby', 'paqc1_monopatin',
               'paqc1_futbol', 'paqc1_voleibol', 'paqc1_hockey', 'paqc1_baloncesto',
               'paqc1_esquiar', 'paqc1_raqueta', 'paqc1_balonmano', 'paqc1_atletismo',
               'paqc1_musculacion', 'paqc1_marciales', 'paqc1_otros', 'paqc2', 'paqc3',
               'paqc4', 'paqc5', 'paqc6', 'paqc7', 'paqc8', 'paqc9_lunes', 'paqc9_martes',
               'paqc9_miercoles', 'paqc9_jueves', 'paqc9_viernes', 'paqc9_sabado', 'paqc9_domingo',
               'pacq10_1', 'paqc10_2']

    df = pd.DataFrame(paqc, index=user_list, columns=columns)

    # print(df)

    return df
