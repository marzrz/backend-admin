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
    users_documents = mongo.db.user.find()
    users = json_util.dumps(users_documents)

    return users


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
