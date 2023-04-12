from flask_cors import CORS
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson import json_util, ObjectId

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
    # users = json_util.dumps(users_documents)
    for user_document in user_documents:
        user = json_util.loads(json_util.dumps(user_document))
        user_list.append(user['_id'])

    response = {
        "users": user_list
    }

    return jsonify(response)


@app.route('/users/<id_user>', methods=['GET'])
def get_user(id):
    user_document = mongo.db.user.find_one({"_id": ObjectId(id)})
    user = json_util.dumps(user_document)

    return user


@app.route('/users/<id_user>/conversations', methods=['GET'])
def get_conversations(id_user):
    user = json_util.loads(func_get_user(id_user))
    conversations = user['conversations']

    return conversations


@app.route('/users/<id_user>/points', methods=['GET'])
def get_points(id_user):
    user = json_util.loads(func_get_user(id_user))
    points = user['points']

    return points


@app.route('/users/<id_user>/kidmed', methods=['GET'])
def get_kidmed(id_user):
    user = json_util.loads(func_get_user(id_user))
    kidmed = user['kidmed']

    return kidmed


@app.route('/users/<id_user>/totalkidmed', methods=['GET'])
def get_totalkidmed(id_user):
    user = json_util.loads(func_get_user(id_user))
    totalkidmed = user['total_kidmed']

    return totalkidmed


@app.route('/users/<id_user>/demtest', methods=['GET'])
def get_demtest(id_user):
    user = json_util.loads(func_get_user(id_user))
    demtest = user['dem_test']

    return demtest


@app.route('/users/<id_user>/paqc', methods=['GET'])
def get_paqc(id_user):
    user = json_util.loads(func_get_user(id_user))
    paqc = user['paqc']

    return paqc


@app.route('/users/<id_user>/pedsql', methods=['GET'])
def get_pedsql(id_user):
    user = json_util.loads(func_get_user(id_user))
    pedsql = user['pedsql']

    return pedsql


@app.route('/users/<id_user>/initialtest', methods=['GET'])
def get_initialtest(id_user):
    user = json_util.loads(func_get_user(id_user))
    initialtest = user['initial_test']

    return initialtest


@app.route('/users/<id_user>/game1part1', methods=['GET'])
def get_game1part1(id_user):
    user = json_util.loads(func_get_user(id_user))
    game1part1 = user['game1_part1']

    return game1part1


@app.route('/users/<id_user>/game1part2', methods=['GET'])
def get_game1part2(id_user):
    user = json_util.loads(func_get_user(id_user))
    game1part2 = user['game1_part2']

    return game1part2


@app.route('/users/<id_user>/game2', methods=['GET'])
def get_game2(id_user):
    user = json_util.loads(func_get_user(id_user))
    game2 = user['game2']

    return game2


@app.route('/users/<id_user>/game3part1', methods=['GET'])
def get_game3part1(id_user):
    user = json_util.loads(func_get_user(id_user))
    game3part1 = user['game3_part1']

    return game3part1


@app.route('/users/<id_user>/game3part2', methods=['GET'])
def get_game3part2(id_user):
    user = json_util.loads(func_get_user(id_user))
    game3part2 = user['game3_part2']

    return game3part2


@app.route('/users/<id_user>/game4', methods=['GET'])
def get_game4(id_user):
    user = json_util.loads(func_get_user(id_user))
    game4 = user['game4']

    return game4


@app.route('/users/<id_user>/survey', methods=['GET'])
def get_game1(id_user):
    user = json_util.loads(func_get_user(id_user))
    survey = user['survey']

    return survey


# CONVERSATION
@app.route('/conversations/<id_conver>', methods=['GET'])
def get_conversation(id_conver):
    conversation_document = mongo.db.conversation.find_one({"_id": ObjectId(id_conver)})
    conversation = json_util.dumps(conversation_document)

    return conversation


if __name__ == '__main__':
    import ssl

    context = ssl.SSLContext()
    context.load_cert_chain("/etc/ssl/certs/conversational_ugr_es.pem", "/etc/ssl/certs/conversational_ugr_es.key")
    CORS(app)
    app.run(host='0.0.0.0', port=5500, ssl_context=context, debug=False)
