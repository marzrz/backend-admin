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
    user_list = []
    columns = []
    columns_complete = False
    n_variables = 20
    user_documents = list(mongo.db.user.find())
    demtest = [[None] * n_variables] * len(user_documents)
    for doc in user_documents:
        demtest[user_documents.index(doc)] = []
        user = json_util.loads(json_util.dumps(doc))
        user_list.append(user['username'])
        if user['initialized'] and user['dem_test_complete']:
            demtest_json = json_util.loads(json_util.dumps(user['dem_test']))
            for info in demtest_json:
                if not columns_complete:
                    columns.append(info)
                demtest[user_documents.index(doc)].append(demtest_json[info])
            columns_complete = True
        else:
            for i in range(0, n_variables):
                demtest[user_documents.index(doc)].append(None)

    df = pd.DataFrame(demtest, index=user_list, columns=columns)

    return df


def kidmed():
    user_list = []
    columns = []
    columns_complete = False
    n_variables = 17
    user_documents = list(mongo.db.user.find())
    kidmed = [[None] * n_variables] * len(user_documents)
    for doc in user_documents:
        kidmed[user_documents.index(doc)] = []
        user = json_util.loads(json_util.dumps(doc))
        user_list.append(user['username'])
        if user['initialized'] and user['kidmed_complete']:
            kidmed_json = json_util.loads(json_util.dumps(user['kidmed']))
            kidmed[user_documents.index(doc)].append(user['total_kidmed'])
            if not columns_complete:
                columns.append('total_kidmed')
            for info in kidmed_json:
                if not columns_complete:
                    columns.append(info)
                kidmed[user_documents.index(doc)].append(kidmed_json[info])
            columns_complete = True
        else:
            for i in range(0, n_variables):
                kidmed[user_documents.index(doc)].append(None)

    df = pd.DataFrame(kidmed, index=user_list, columns=columns)

    return df


def paqc():
    user_list = []
    columns = []
    columns_complete = False
    n_variables = 39
    user_documents = list(mongo.db.user.find())
    paqc = [[None] * n_variables] * len(user_documents)
    for doc in user_documents:
        paqc[user_documents.index(doc)] = []
        user = json_util.loads(json_util.dumps(doc))
        user_list.append(user['username'])
        if user['initialized'] and user['paqc_complete']:
            paqc_json = json_util.loads(json_util.dumps(user['paqc']))
            for info in paqc_json:
                paqcItem_json = json_util.loads(json_util.dumps(paqc_json[info]))
                if info == 'paqc_1':
                    for sport in paqcItem_json:
                        if not columns_complete:
                            columns.append('paq1_' + sport)
                        paqc[user_documents.index(doc)].append(paqcItem_json[sport])
                elif info == 'paqc_9':
                    for day in paqcItem_json:
                        if not columns_complete:
                            columns.append('paq9_' + day)
                        paqc[user_documents.index(doc)].append(paqcItem_json[day])
                elif info == 'paqc_10':
                    for question in paqcItem_json:
                        if not columns_complete:
                            columns.append('paq10_' + question)
                        paqc[user_documents.index(doc)].append(paqcItem_json[question])
                else:
                    if not columns_complete:
                        columns.append(info)
                    paqc[user_documents.index(doc)].append(paqcItem_json)
            columns_complete = True
        else:
            for i in range(0, n_variables):
                paqc[user_documents.index(doc)].append(None)

    df = pd.DataFrame(paqc, index=user_list, columns=columns)

    return df


def pedsql():
    user_list = []
    columns = []
    columns_complete = False
    n_variables = 23
    user_documents = list(mongo.db.user.find())
    pedsql = [[None] * n_variables] * len(user_documents)
    for doc in user_documents:
        pedsql[user_documents.index(doc)] = []
        user = json_util.loads(json_util.dumps(doc))
        user_list.append(user['username'])
        if user['initialized'] and user['pedsql_complete']:
            pedsql_json = json_util.loads(json_util.dumps(user['pedsql']))
            for info in pedsql_json:
                pedsqlItem_json = json_util.loads(json_util.dumps(pedsql_json[info]))
                if info == 'salud_actividades':
                    for salud in pedsqlItem_json:
                        if not columns_complete:
                            columns.append(salud)
                        pedsql[user_documents.index(doc)].append(pedsqlItem_json[salud])
                elif info == 'sentimientos':
                    for sentimiento in pedsqlItem_json:
                        if not columns_complete:
                            columns.append(sentimiento)
                        pedsql[user_documents.index(doc)].append(pedsqlItem_json[sentimiento])
                elif info == 'relaciones':
                    for relacion in pedsqlItem_json:
                        if not columns_complete:
                            columns.append(relacion)
                        pedsql[user_documents.index(doc)].append(pedsqlItem_json[relacion])
                elif info == 'escolares':
                    for escolar in pedsqlItem_json:
                        if not columns_complete:
                            columns.append(escolar)
                        pedsql[user_documents.index(doc)].append(pedsqlItem_json[escolar])
            columns_complete = True
        else:
            for i in range(0, n_variables):
                pedsql[user_documents.index(doc)].append(None)

    df = pd.DataFrame(pedsql, index=user_list, columns=columns)

    return df


def initialtest():
    user_list = []
    columns = []
    columns_complete = False
    n_variables = 18
    user_documents = list(mongo.db.user.find())
    initialtest = [[None] * n_variables] * len(user_documents)
    for doc in user_documents:
        initialtest[user_documents.index(doc)] = []
        user = json_util.loads(json_util.dumps(doc))
        user_list.append(user['username'])
        if user['initialized'] and user['initial_test_complete']:
            initialtest_json = json_util.loads(json_util.dumps(user['initial_test']))
            for info in initialtest_json:
                if not columns_complete:
                    columns.append(info)
                initialtest[user_documents.index(doc)].append(initialtest_json[info])
            columns_complete = True
        else:
            for i in range(0, n_variables):
                initialtest[user_documents.index(doc)].append(None)

    df = pd.DataFrame(initialtest, index=user_list, columns=columns)

    return df


def game1():
    user_list = []
    columns = []
    columns_complete = False
    n_variables = 152
    user_documents = list(mongo.db.user.find())
    game1 = [[None] * n_variables] * len(user_documents)
    for doc in user_documents:
        game1[user_documents.index(doc)] = []
        user = json_util.loads(json_util.dumps(doc))
        user_list.append(user['username'])
        if user['initialized'] and user['game1_part2_complete']:
            game1_json = json_util.loads(json_util.dumps(user['game1']))
            if not columns_complete:
                columns.append('g1p1_points')
            game1[user_documents.index(doc)].append(game1_json['totalPoints'])
            for info in range(0, len(game1_json['questions'])):
                if not columns_complete:
                    columns.append('g1p1_q' + str(info + 1) + '_question')
                    columns.append('g1p1_q' + str(info + 1) + '_answer')
                    columns.append('g1p1_q' + str(info + 1) + '_value')
                game1[user_documents.index(doc)].append(game1_json['questions'][info]['question'])
                game1[user_documents.index(doc)].append(game1_json['questions'][info]['answer']['answer'])
                game1[user_documents.index(doc)].append(game1_json['questions'][info]['answer']['value'])
            game1_part2_json = json_util.loads(json_util.dumps(user['game1_part2']))
            if not columns_complete:
                columns.append('g1p2_points')
            game1[user_documents.index(doc)].append(game1_part2_json['totalPoints'])
            for info in range(0, len(game1_part2_json['questions'])):
                if not columns_complete:
                    columns.append('g1p2_q' + str(info + 1) + '_question')
                    columns.append('g1p2_q' + str(info + 1) + '_nutrient')
                    columns.append('g1p2_q' + str(info + 1) + '_nutrient_value')
                    columns.append('g1p2_q' + str(info + 1) + '_foodgroup')
                    columns.append('g1p2_q' + str(info + 1) + '_foodgroup_value')
                game1[user_documents.index(doc)].append(game1_part2_json['questions'][info]['question'])
                game1[user_documents.index(doc)].append(game1_part2_json['questions'][info]['nutrient']['text'])
                game1[user_documents.index(doc)].append(game1_part2_json['questions'][info]['nutrient']['value'])
                game1[user_documents.index(doc)].append(game1_part2_json['questions'][info]['food_group']['text'])
                game1[user_documents.index(doc)].append(game1_part2_json['questions'][info]['food_group']['value'])
            columns_complete = True
        else:
            for i in range(0, n_variables):
                game1[user_documents.index(doc)].append(None)

    df = pd.DataFrame(game1, index=user_list, columns=columns)

    return df


def game2():
    user_list = []
    columns = []
    columns_complete = False
    n_variables = 19
    user_documents = list(mongo.db.user.find())
    game2 = [[None] * n_variables] * len(user_documents)
    for doc in user_documents:
        game2[user_documents.index(doc)] = []
        user = json_util.loads(json_util.dumps(doc))
        user_list.append(user['username'])
        if user['initialized'] and user['game2_complete']:
            game2_json = json_util.loads(json_util.dumps(user['game2']))
            if not columns_complete:
                columns.append('g2_points')
            game2[user_documents.index(doc)].append(game2_json['totalPoints'])
            for info in range(0, len(game2_json['questions'])):
                if not columns_complete:
                    columns.append('g2_q' + str(info + 1) + '_question')
                    columns.append('g2_q' + str(info + 1) + '_answer')
                    columns.append('g2_q' + str(info + 1) + '_value')
                game2[user_documents.index(doc)].append(game2_json['questions'][info]['question'])
                game2[user_documents.index(doc)].append(game2_json['questions'][info]['answer']['answer'])
                game2[user_documents.index(doc)].append(game2_json['questions'][info]['answer']['value'])
            columns_complete = True
        else:
            for i in range(0, n_variables):
                game2[user_documents.index(doc)].append(None)

    df = pd.DataFrame(game2, index=user_list, columns=columns)

    return df


def game3():
    user_list = []
    columns = []
    columns_complete = False
    n_variables = 5
    user_documents = list(mongo.db.user.find())
    game3 = [[None] * n_variables] * len(user_documents)
    for doc in user_documents:
        game3[user_documents.index(doc)] = []
        user = json_util.loads(json_util.dumps(doc))
        user_list.append(user['username'])
        if user['initialized'] and user['game3_part2_complete']:
            game3_json = json_util.loads(json_util.dumps(user['game3']))
            if not columns_complete:
                columns.append('g3p1_points')
            game3[user_documents.index(doc)].append(game3_json['totalPoints'])
            for info in range(0, len(game3_json['questions'])):
                if not columns_complete:
                    columns.append('g3p1_q' + str(info + 1) + '_question')
                    columns.append('g3p1_q' + str(info + 1) + '_answer')
                    columns.append('g3p1_q' + str(info + 1) + '_value')
                game3[user_documents.index(doc)].append(game3_json['questions'][info]['question'])
                game3[user_documents.index(doc)].append(game3_json['questions'][info]['answer']['answer'])
                game3[user_documents.index(doc)].append(game3_json['questions'][info]['answer']['value'])
            game3_part2_json = json_util.loads(json_util.dumps(user['game3_part2']))
            if not columns_complete:
                columns.append('g3p2_points')
            game3[user_documents.index(doc)].append(game3_part2_json['totalPoints'])
            for info in range(0, len(game3_part2_json['questions'])):
                if not columns_complete:
                    columns.append('g3p2_q' + str(info + 1) + '_question')
                    columns.append('g3p2_q' + str(info + 1) + '_answer')
                    columns.append('g3p2_q' + str(info + 1) + '_value')
                game3[user_documents.index(doc)].append(game3_part2_json['questions'][info]['question'])
                game3[user_documents.index(doc)].append(game3_part2_json['questions'][info]['answer']['answer'])
                game3[user_documents.index(doc)].append(game3_part2_json['questions'][info]['answer']['value'])
            columns_complete = True
        else:
            for i in range(0, n_variables):
                game3[user_documents.index(doc)].append(None)

    df = pd.DataFrame(game3, index=user_list, columns=columns)

    return df


def game4():
    user_list = []
    columns = []
    columns_complete = False
    n_variables = 17
    user_documents = list(mongo.db.user.find())
    game4 = [[None] * n_variables] * len(user_documents)
    for doc in user_documents:
        game4[user_documents.index(doc)] = []
        user = json_util.loads(json_util.dumps(doc))
        user_list.append(user['username'])
        if user['initialized'] and user['game4_complete']:
            game4_json = json_util.loads(json_util.dumps(user['game4']))
            if not columns_complete:
                columns.append('g4_points')
            game4[user_documents.index(doc)].append(game4_json['totalPoints'])
            for info in range(0, len(game4_json['questions'])):
                if not columns_complete:
                    columns.append('g4_q' + str(info + 1) + '_answer')
                    columns.append('g4_q' + str(info + 1) + '_value')
                game4[user_documents.index(doc)].append(game4_json['questions'][info]['answer']['answer'])
                game4[user_documents.index(doc)].append(game4_json['questions'][info]['answer']['value'])
            columns_complete = True
        else:
            for i in range(0, n_variables):
                game4[user_documents.index(doc)].append(None)

    df = pd.DataFrame(game4, index=user_list, columns=columns)

    return df


def survey():
    user_list = []
    columns = []
    columns_complete = False
    n_variables = 10
    user_documents = list(mongo.db.user.find())
    survey = [[None] * n_variables] * len(user_documents)
    for doc in user_documents:
        survey[user_documents.index(doc)] = []
        user = json_util.loads(json_util.dumps(doc))
        user_list.append(user['username'])
        if user['initialized'] and user['survey_complete']:
            survey_json = json_util.loads(json_util.dumps(user['survey']))
            for info in range(0, len(survey_json)):
                if survey_json[info]['yesOrNo']:
                    if not columns_complete:
                        columns.append('survey_' + str(info + 1))
                    survey[user_documents.index(doc)].append(survey_json[info]['value'])
                    if survey_json[info]['inputText']:
                        if not columns_complete:
                            columns.append('survey_' + str(info + 1) + '_text')
                        survey[user_documents.index(doc)].append(survey_json[info]['text'])
                else:
                    if not columns_complete:
                        columns.append('survey_' + str(info + 1))
                    survey[user_documents.index(doc)].append(survey_json[info]['value'])
            columns_complete = True
        else:
            for i in range(0, n_variables):
                survey[user_documents.index(doc)].append(None)

    df = pd.DataFrame(survey, index=user_list, columns=columns)

    return df


def pretests(number):
    df_list = []
    data_list = []
    user_list = []
    columns = []
    columns_complete = False
    n_variables = 97
    user_documents = list(mongo.db.user.find())
    pretest = [[None] * n_variables] * len(user_documents)
    for doc in user_documents:
        pretest[user_documents.index(doc)] = []
        user = json_util.loads(json_util.dumps(doc))
        user_list.append(user['username'])
        if user['initialized'] and user['pretest_complete'] >= number:
            pretest_list = json_util.loads(json_util.dumps(user['pretests']))
            pretest_document = mongo.db.pretest.find_one({'_id': pretest_list[number-1]})
            pretest_json = json_util.loads(json_util.dumps(pretest_document))
            if not columns_complete:
                columns.append('ev' + str(number) + '_points')
            pretest[user_documents.index(doc)].append(pretest_json['totalPoints'])
            for question in range(0, len(pretest_json['questions'])):
                if not columns_complete:
                    columns.append('ev' + str(number) + '_q' + str(question + 1) + '_question')
                    columns.append('ev' + str(number) + '_q' + str(question + 1) + '_answer')
                    columns.append('ev' + str(number) + '_q' + str(question + 1) + '_value')
                pretest[user_documents.index(doc)].append(pretest_json['questions'][question]['question'])
                pretest[user_documents.index(doc)].append(pretest_json['questions'][question]['answer']['answer'])
                pretest[user_documents.index(doc)].append(pretest_json['questions'][question]['answer']['value'])
            columns_complete = True
        else:
            for i in range(0, n_variables):
                pretest[user_documents.index(doc)].append(None)

    print(len(columns))

    df = pd.DataFrame(pretest, index=user_list, columns=columns)

    return df

