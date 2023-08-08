from flask import jsonify, request
import requests

from server.config import get_config


def wx_login(self):
        code = request.json.get('code')
        if code:
            wx = get_config('weixin')
            appid = wx['appid']
            secret = wx['secret']
            # 向微信服务器请求获取 openid 和 session_key
            response = requests.get(
                f'https://api.weixin.qq.com/sns/jscode2session?appid={appid}&secret={secret}&js_code={code}&grant_type=authorization_code')
            data = response.json()
            openid = data.get('openid')

            return jsonify({'openid': openid})
        else:
            return jsonify({'error': 'Invalid request'})