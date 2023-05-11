import datetime

from flask_cors import CORS
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson import json_util, ObjectId
import pandas as pd
import data
import os

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/bon-app-petit"
mongo = PyMongo(app)


# FUNCTIONS
def func_get_user(id):
    user_document = mongo.db.user.find_one({"_id": ObjectId(id)})
    user = json_util.dumps(user_document)

    return user


# USER
@app.route('/users', methods=['GET'])
def get_users():
    user_list = []
    user_documents = mongo.db.user.find()
    for doc in user_documents:
        user = json_util.loads(json_util.dumps(doc))
        user = {
            'id_user': str(user['_id']),
            'username': user['username'],
            'initialized': user['initialized']
        }
        user_list.append(user)

    response = {
        'users': user_list
    }

    return jsonify(response)


@app.route('/users/<id_user>/user', methods=['GET'])
def get_user(id_user):
    user_document = mongo.db.user.find_one({"_id": ObjectId(id_user)})
    user = json_util.loads(json_util.dumps(user_document))

    response = {
        'username': user['username'],
        'id_user': str(user['_id']),
        'initialized': user['initialized']
    }

    return jsonify(response)


@app.route('/users/<id_user>/conversations', methods=['GET'])
def get_conversations(id_user):
    conversation_list = []
    user = json_util.loads(func_get_user(id_user))
    if user['initialized']:
        conversations = user['conversations']
        for conver in conversations:
            conversation_document = mongo.db.conversation.find_one({"_id": conver})
            if conversation_document:
                conversation = json_util.loads(json_util.dumps(conversation_document))
                conver_item = {
                    'id_conver': str(conver),
                    'session': conversation['session'],
                    'n_messages': len(conversation['messages']),
                    'date': conversation['messages'][0]['date']
                }
                conversation_list.append(conver_item)

    response = {
        'conversations': conversation_list
    }

    return jsonify(response)


@app.route('/users/<id_user>/points', methods=['GET'])
def get_points(id_user):
    user = json_util.loads(func_get_user(id_user))
    points = user['points']

    response = {
        'points': points
    }

    return jsonify(response)

@app.route('/users/kidmed', methods=['GET'])
def get_kidmed_all():
    tests = []
    users = []
    user_documents = mongo.db.user.find()
    for doc in user_documents:
        user = json_util.loads(json_util.dumps(doc))
        if user['initialized']:
            kidmed = {
                'kidmed': user['kidmed'],
                'points': user['total_kidmed']
            }
            tests.append(kidmed)
            users.append(user['username'])

    response = {
        'tests': tests,
        'users': users
    }

    return jsonify(response)

@app.route('/users/<id_user>/kidmed', methods=['GET'])
def get_kidmed(id_user):
    user = json_util.loads(func_get_user(id_user))
    kidmed = user['kidmed']
    points = user['total_kidmed']

    response = {
        'kidmed': kidmed,
        'points': points
    }

    return jsonify(response)


@app.route('/users/<id_user>/demtest', methods=['GET'])
def get_demtest(id_user):
    user = json_util.loads(func_get_user(id_user))
    demtest = user['dem_test']

    return demtest

@app.route('/users/demtest', methods=['GET'])
def get_demtest_all():
    tests = []
    users = []
    user_documents = mongo.db.user.find()
    for doc in user_documents:
        user = json_util.loads(json_util.dumps(doc))
        if user['initialized']:
            tests.append(user['dem_test'])
            users.append(user['username'])

    response = {
        'tests': tests,
        'users': users
    }

    return jsonify(response)


@app.route('/users/<id_user>/paqc', methods=['GET'])
def get_paqc(id_user):
    user = json_util.loads(func_get_user(id_user))
    paqc = user['paqc']

    return paqc

@app.route('/users/paqc', methods=['GET'])
def get_paqc_all():
    tests = []
    users = []
    user_documents = mongo.db.user.find()
    for doc in user_documents:
        user = json_util.loads(json_util.dumps(doc))
        if user['initialized']:
            tests.append(user['paqc'])
            users.append(user['username'])

    response = {
        'tests': tests,
        'users': users
    }

    return jsonify(response)


@app.route('/users/<id_user>/pedsql', methods=['GET'])
def get_pedsql(id_user):
    user = json_util.loads(func_get_user(id_user))
    pedsql = user['pedsql']

    return pedsql

@app.route('/users/pedsql', methods=['GET'])
def get_pedsql_all():
    tests = []
    users = []
    user_documents = mongo.db.user.find()
    for doc in user_documents:
        user = json_util.loads(json_util.dumps(doc))
        if user['initialized']:
            tests.append(user['pedsql'])
            users.append(user['username'])

    response = {
        'tests': tests,
        'users': users
    }

    return jsonify(response)


@app.route('/users/<id_user>/initialtest', methods=['GET'])
def get_initialtest(id_user):
    user = json_util.loads(func_get_user(id_user))
    initialtest = user['initial_test']

    return initialtest

@app.route('/users/initialtest', methods=['GET'])
def get_initialtest_all():
    tests = []
    users = []
    user_documents = mongo.db.user.find()
    for doc in user_documents:
        user = json_util.loads(json_util.dumps(doc))
        if user['initialized']:
            tests.append(user['initial_test'])
            users.append(user['username'])

    response = {
        'tests': tests,
        'users': users
    }

    return jsonify(response)


@app.route('/users/<id_user>/game/<id_game>', methods=['GET'])
def get_game(id_user, id_game):
    user = json_util.loads(func_get_user(id_user))
    game1_1 = user['game1']
    game1_2 = user['game1_part2']
    game2 = user['game2']
    game3_1 = user['game3']
    game3_2 = user['game3_part2']
    game4 = user['game4']

    game1_completed = user['game1_part2_complete']
    game2_completed = user['game2_complete']
    game3_completed = user['game3_part2_complete']
    game4_completed = user['game4_complete']

    if id_game == "1":
        if game1_completed:
            response = {
                'questions_1': game1_1['questions'],
                'points_1': game1_1['totalPoints'],
                'questions_2': game1_2['questions'],
                'points_2': game1_2['totalPoints']
            }
        else:
            response = {
                'status': 'Game 1 not completed'
            }
    elif id_game == "2":
        if game2_completed:
            response = {
                'questions': game2['questions'],
                'points': game2['totalPoints']
            }
        else:
            response = {
                'status': 'Game 2 not completed'
            }
    elif id_game == "3":
        if game3_completed:
            response = {
                'questions_1': game3_1['questions'],
                'points_1': game3_1['totalPoints'],
                'questions_2': game3_2['questions'],
                'points_2': game3_2['totalPoints']
            }
        else:
            response = {
                'status': 'Game 3 not completed'
            }
    elif id_game == "4":
        if game4_completed:
            response = {
                'questions': game4['questions'],
                'points': game4['totalPoints']
            }
        else:
            response = {
                'status': 'Game 4 not completed'
            }
    else:
        response = {
            'status': 'Error',
            'user': id_user,
            'game': id_game
        }

    return jsonify(response)

@app.route('/users/games/<id_game>', methods=['GET'])
def get_game_all(id_game):
    tests = []
    users = []
    user_documents = mongo.db.user.find()
    for doc in user_documents:
        user = json_util.loads(json_util.dumps(doc))
        if user['initialized']:
            if user['game1_part2_complete']:
                game1_1 = user['game1']
            else:
                game1_1 = user['game1_part1']
            game1_2 = user['game1_part2']
            game2 = user['game2']
            if user['game3_part2_complete']:
                game3_1 = user['game3']
            else:
                game3_1 = user['game3_part1']
            game3_2 = user['game3_part2']
            game4 = user['game4']

            users.append(user['username'])

            if id_game == "1":
                if user['game1_part2_complete']:
                    data = {
                        'questions_1': game1_1['questions'],
                        'points_1': game1_1['totalPoints'],
                        'questions_2': game1_2['questions'],
                        'points_2': game1_2['totalPoints']
                    }
                else:
                    data = {
                        'questions_1': [],
                        'points_1': None,
                        'questions_2': [],
                        'points_2': None
                    }
                tests.append(data)
            elif id_game == "2":
                if user['game2_complete']:
                    data = {
                        'questions': game2['questions'],
                        'points': game2['totalPoints']
                    }
                else:
                    data = {
                        'questions': [],
                        'points': None
                    }
                tests.append(data)
            elif id_game == "3":
                if user['game3_part2_complete']:
                    data = {
                        'questions_1': game3_1['questions'],
                        'points_1': game3_1['totalPoints'],
                        'questions_2': game3_2['questions'],
                        'points_2': game3_2['totalPoints']
                    }
                else:
                    data = {
                        'questions_1': [],
                        'points_1': None,
                        'questions_2': [],
                        'points_2': None
                    }
                tests.append(data)
            elif id_game == "4":
                if user['game4_complete']:
                    data = {
                        'questions': game4['questions'],
                        'points': game4['totalPoints']
                    }
                else:
                    data = {
                        'questions': [],
                        'points': None
                    }
                tests.append(data)

    response = {
        'tests': tests,
        'users': users
    }

    return jsonify(response)


@app.route('/users/<id_user>/survey', methods=['GET'])
def get_game1(id_user):
    user = json_util.loads(func_get_user(id_user))
    survey = user['survey']

    return survey

@app.route('/users/survey', methods=['GET'])
def get_survey_all():
    tests = []
    users = []
    user_documents = mongo.db.user.find()
    for doc in user_documents:
        user = json_util.loads(json_util.dumps(doc))
        if user['initialized']:
            tests.append(user['survey'])
            users.append(user['username'])

    response = {
        'tests': tests,
        'users': users
    }

    return jsonify(response)


@app.route('/users/<id_user>/pretests', methods=['GET'])
def get_pretests(id_user):
    pretest_list = []
    user = json_util.loads(func_get_user(id_user))
    pretests = user['pretests']
    for test in pretests:
        test = {
            'id_test': str(test),
            'index': pretests.index(test) + 1
        }
        pretest_list.append(test)

    response = {
        'pretests': pretest_list
    }

    return jsonify(response)


# PRETEST
@app.route('/pretests/<id_test>', methods=['GET'])
def get_pretest(id_test):
    pretest_document = mongo.db.pretest.find_one({"_id": ObjectId(id_test)})
    pretest = json_util.loads(json_util.dumps(pretest_document))

    response = {
        'id': str(pretest['_id']),
        'questions': pretest['questions'],
        'points': pretest['totalPoints']
    }

    return jsonify(response)

@app.route('/users/pretests/<index_test>', methods=['GET'])
def get_all_pretests(index_test):
    tests = []
    users = []
    points = []
    user_documents = mongo.db.user.find()
    for doc in user_documents:
        user = json_util.loads(json_util.dumps(doc))
        if user['initialized']:
            if len(user['pretests']) > int(index_test):
                pretest_document = mongo.db.pretest.find_one({"_id": ObjectId(user['pretests'][int(index_test)])})
                pretest = json_util.loads(json_util.dumps(pretest_document))
                tests.append(pretest['questions'])
                points.append(pretest['totalPoints'])
                users.append(user['username'])
            else:
                tests.append([])
                points.append(None)
                users.append(user['username'])

    response = {
        'tests': tests,
        'points': points,
        'users': users
    }

    return jsonify(response)


# CONVERSATION
@app.route('/conversations/<id_conver>', methods=['GET'])
def get_conversation(id_conver):
    conversation_document = mongo.db.conversation.find_one({"_id": ObjectId(id_conver)})
    conversation = json_util.loads(json_util.dumps(conversation_document))

    response = {
        'id': str(conversation['_id']),
        'session': conversation['session'],
        'messages': conversation['messages']
    }

    return jsonify(response)


@app.route('/conversations/<id_conver>/params', methods=['GET'])
def get_parameters(id_conver):
    conversation_document = mongo.db.conversation.find_one({"_id": ObjectId(id_conver)})
    conversation = json_util.loads(json_util.dumps(conversation_document))
    last_message_index = len(conversation['messages']) - 1

    if conversation['messages'][last_message_index]['user'] == 'user':
        last_message_index -= 1

    response = {
        'params': conversation['messages'][last_message_index]['parameters']
    }

    return jsonify(response)


# LOGIN
@app.route('/login', methods=['POST'])
def login():
    username = request.json["username"]
    password = request.json["password"]
    userDocument = mongo.db.admin.find_one({"username": username, "password": password})

    if (userDocument):
        user = json_util.loads(json_util.dumps(userDocument))
        objectId = str(user['_id'])
        data = {
            'exists': True,
            'token': objectId
        }
    else:
        data = {
            'exists': False,
            'token': ''
        }

    return jsonify(data)

# EXPORT
@app.route('/exports/xlsx', methods=['GET'])
def export_xlsx():
    file = '/home/marina/dev/backend-admin/data_bonappetit.xlsx'
    demtest = data.demtest()
    kidmed = data.kidmed()
    paqc = data.paqc()
    pedsql = data.pedsql()
    initialtest = data.initialtest()
    pretest1 = data.pretests(1)
    pretest2 = data.pretests(2)
    pretest3 = data.pretests(3)
    game1 = data.game1()
    game2 = data.game2()
    game3 = data.game3()
    game4 = data.game4()
    survey = data.survey()

    with pd.ExcelWriter(file) as writer:
        demtest.to_excel(writer, sheet_name='Test demográfico')
        kidmed.to_excel(writer, sheet_name='Kidmed')
        paqc.to_excel(writer, sheet_name='Paq-C')
        pedsql.to_excel(writer, sheet_name='PedsQL')
        initialtest.to_excel(writer, sheet_name='Test hábitos alimenticios')
        pretest1.to_excel(writer, sheet_name='Evaluación 1')
        pretest2.to_excel(writer, sheet_name='Evaluación 2')
        pretest3.to_excel(writer, sheet_name='Evaluación 3')
        game1.to_excel(writer, sheet_name='Juego 1')
        game2.to_excel(writer, sheet_name='Juego 2')
        game3.to_excel(writer, sheet_name='Juego 3')
        game4.to_excel(writer, sheet_name='Juego 4')
        survey.to_excel(writer, sheet_name='Encuesta')

    response = {
        'file': 'https://conversational.ugr.es/bonappetit/uws3d/static/data_bonappetit.xlsx'
    }

    return jsonify(response)

@app.route('/exports/xlsx/<test>', methods=['GET'])
def export_xlsx_test(test):
    test_data = ''
    file = '/home/marina/dev/backend-admin/data_bonappetit_'+test+'.xlsx'
    if test == 'demtest':
        test_data = data.demtest()
    if test == 'kidmed':
        test_data = data.kidmed()
    if test == 'paqc':
        test_data = data.paqc()
    if test == 'pedsql':
        test_data = data.pedsql()
    if test == 'initialtest':
        test_data = data.initialtest()
    if test == 'pretest1':
        test_data = data.pretests(1)
    if test == 'pretest2':
        test_data = data.pretests(2)
    if test == 'pretest3':
        test_data = data.pretests(3)
    if test == 'game1':
        test_data = data.game1()
    if test == 'game2':
        test_data = data.game2()
    if test == 'game3':
        test_data = data.game3()
    if test == 'game4':
        test_data = data.game4()

    test_data.to_excel(file)

    response = {
        'file': 'https://conversational.ugr.es/bonappetit/uws3d/static/data_bonappetit_'+test+'.xlsx'
    }

    return jsonify(response)


if __name__ == '__main__':
    import ssl

    context = ssl.SSLContext()
    context.load_cert_chain("/etc/ssl/certs/conversational_ugr_es.pem", "/etc/ssl/certs/conversational_ugr_es.key")
    CORS(app)
    app.run(host='0.0.0.0', port=5500, ssl_context=context, debug=False)