import json
from flask import render_template, redirect, url_for
from time import time
from os import urandom


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
            }
        }

    def _chat(self, conversation_id):
        if '-' not in conversation_id:
            return redirect(url_for('._index'))

        return render_template('index.html', chat_id=conversation_id)

    def _index(self):
        return render_template('index.html', chat_id=f'{urandom(4).hex()}-{urandom(2).hex()}-{urandom(2).hex()}-{urandom(2).hex()}-{hex(int(time() * 1000))[2:]}', url_prefix=self.url_prefix)

    def _model_info(self, user_id):
        data = [
            {
                'name': 'GPT4All-J v1.3-groovy',
                'value': "gpt4all",
                'select': False,
                'content': '创意模型可用于商业用途;\
                快速响应;\
                创意回应;\
                基于指令;\
                由 Nomic AI. 培训;'
            }, {
                'name': 'gpt-3.5-turbo-16k-0613',
                'select': False,
                'value': "gpt-3.5-turbo-16k-0613",
                'content': '-GPT3.5 Turbo,Training data as of September 2021'
            },{
                'name': 'dify.ai',
                'select': True,
                'value': "dify-ai",
                'content': '-GPT3.5 Turbo,Training data as of September 2021'
            },
        ]

        res_json = json.dumps(data)

        return res_json
