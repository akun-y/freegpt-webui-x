import json
from flask import jsonify, render_template, redirect, request, url_for
from time import time
from os import urandom

import requests

from server.model_info import get_model_info, post_model_info
from server.weixin import wx_login


class Website:
    def __init__(self, bp, url_prefix) -> None:
        self.bp = bp
        self.url_prefix = url_prefix
        self.routes = {
            '/': {
                'function': lambda: redirect(url_for('._index')),
                'methods': ['GET', 'POST']
            },
            '/chat/': {
                'function': self._index,
                'methods': ['GET', 'POST']
            },
            '/chat/<conversation_id>': {
                'function': self._chat,
                'methods': ['GET', 'POST']
            },
            '/user/model/<user_id>': {
                'function': self._model_info,
                'methods': ['GET', 'POST']
            },
            '/user/wx/login': {
                'function': self._wx_login,
                'methods': ['POST']
            }
        }

    def _chat(self, conversation_id):
        if '-' not in conversation_id:
            return redirect(url_for('._index'))

        return render_template('index.html', chat_id=conversation_id)

    def _index(self):
        return render_template('index.html', chat_id=f'{urandom(4).hex()}-{urandom(2).hex()}-{urandom(2).hex()}-{urandom(2).hex()}-{hex(int(time() * 1000))[2:]}', url_prefix=self.url_prefix)

    def _model_info(self, user_id):
        if request.method == 'POST':
            return post_model_info(self,request.data)
        else:
            return get_model_info(self,user_id)

    def _wx_login(self):
        return wx_login(self)
