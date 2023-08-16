import json
import re
import time

import requests
from database.chat_table import insert_chat_record
import g4f
import langid
from g4f import ChatCompletion
from googletrans import Translator
from flask import app, request, Response, stream_with_context
from datetime import datetime
from requests import get
from server.config import get_config, special_instructions
from flask import current_app
import logging

from server.logger import init_logger
from server.msgsender import MsgSender


logger = init_logger("services")


class Services_Api:
    def __init__(self, bp, config: dict) -> None:
        wx = get_config('weixin')
        self.appid = wx['appid']
        self.appSecret = wx['secret']
        self.bp = bp
        self.routes = {
            '/services-api/replay': {
                'function': self._replyMsg,
                'methods': ['POST']
            }    ,
            '/services-api/mp_replay': {
                'function': self._mp_replyMsg,
                'methods': ['POST']
            }
        }

    def _replyMsg(self):

        url_access_token = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=' + \
            self.appid + '&secret=' + self.appSecret

        tokenRes = requests.get(url_access_token)

        token = json.loads(tokenRes.text).get('access_token')

        print(token)

        url_msg = 'https://api.weixin.qq.com/cgi-bin/message/subscribe/send'
        body = {
            "touser": "o-yTD5Dp1Qh1hvIJxy1emSuyGBpM",  # 也就是OPENID
            "template_id": "2qEyKWroujGpcdThNhz52uAGwyIp8UAKjB_a2n7Ge-Y",
            "page": "pages/services/services",
            "form_id": "FORMID",  # 这个应该是来源场景值ID吧，我这里没有用到
            "miniprogram_state": "developer",#developer开发版；trial体验版；formal正式版；默认正式版
            "data": {
                "date6": {
                    "value": "2020-03-19 14:35:30"
                },
                # 回复内容
                "thing2": {
                    "value": "你的情况比较乐观，后续定期检查即可"
                },
                # 留言内容
                "thing1": {
                    "value": "服务器内存低于256MB"
                }
            }
        }

        try:
            res = requests.post(url=url_msg, params={
                'access_token': token  # 这里是我们上面获取到的token
            }, data=json.dumps(body, ensure_ascii=False).encode('utf-8'))

            print(res.text)
            r = Response(stream_with_context(res.text),
                         mimetype='text/event-stream')
            r.headers['conversation_id'] = 'Custom Value'
            if(r.status_code == 200):
                print("success")

            return r
        except Exception as e:
            logger.error(e)
            logger.error(e.__traceback__.tb_next)
            time.sleep(3)  # Wait 3 second before trying again
    def _mp_replyMsg(self):
        
        # 使用示例
        sender = MsgSender(appid='wx0b93d5a07a8b876b', appSecret='6460579a622b4fdf2b22f04d9da67511') 
        ret = sender.send(touser='o1ORS1hWyQvM9eqW7OczUzQhr8Xg', content='你好')  
        return "ok" if ret else "error"