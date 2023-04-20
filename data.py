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
