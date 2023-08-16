import json
import requests

class MsgSender:

  def __init__(self, appid, appSecret):
    self.appid = appid
    self.appSecret = appSecret

  def send(self, touser, content):
    
    # 获取access_token
    url_token = f'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={self.appid}&secret={self.appSecret}'
    token_res = requests.get(url_token)
    token = json.loads(token_res.text).get('access_token')
    if not token:
        print('获取access_token失败',token_res.text)
        return False
    # 构造请求数据
    data = {
        "touser": touser,
        "msgtype": "text",
        "text": {
          "content": content
        }
    }

    # 发送消息
    url_msg = f'https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token={token}'
    res = requests.post(url_msg, json=data)

    if res.status_code == 200:
      print('消息发送成功',res.text)
      return True
    else:
      print('消息发送失败',res.text)
      return False

# # 使用示例
# sender = MsgSender(appid='xxx', appSecret='xxx') 
# sender.send(touser='o1ORS1hWyQvM9eqW7OczUzQhr8Xg', content='你好')