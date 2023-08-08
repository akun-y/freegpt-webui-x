# model_info.py

import json
from flask import jsonify

from database.database import UserDatabase
from server.config import get_config


def get_model_info(self, userId):
    db = UserDatabase()
    choice = db.get_choice(userId)

    if choice:
        res_json = json.loads(choice)
    else:
        res_json = get_config('models')
    print(f"用户{userId}的models:", res_json)

    return res_json


def post_model_info(self, data):
    body = json.loads(data)
    print('post_model_info :', body)

    db = UserDatabase()
    db.record_choice(body['userId'], json.dumps(body['models']))

    return jsonify(body)
