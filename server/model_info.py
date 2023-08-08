# model_info.py

import json
from flask import jsonify

from database.database import UserDatabase


def get_model_info(self, userId):
    db = UserDatabase()
    choice = db.get_choice(userId)

    res_json = json.dumps(choice)
    print(f"用户{userId}的models:", res_json)

    return res_json


def post_model_info(self, data):
    body = json.loads(data)
    print('post_model_info :', body)

    db = UserDatabase()
    db.record_choice(body['userId'], json.dumps(body['models']))

    return jsonify(body)
