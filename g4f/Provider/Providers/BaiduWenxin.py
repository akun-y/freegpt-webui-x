import uuid
import requests
import os
import json
from g4f.utils import Utils
from server.config import get_config

from server.logger import init_logger
from ...typing import sha256, Dict, get_type_hints

url = 'https://aip.baidubce.com'
model = ['gpt-3.5-turbo-16k', 'gpt-3.5-turbo-0613']
supports_stream = True
needs_auth = False
logger = init_logger('baidu-wenxin')


wenxin = get_config('baidu_wenxin')
conversations = {}


def _create_completion(model: str, messages: list, stream: bool, temperature: float = 0.4, **kwargs):
    global logger, apikey, conversations

    chatId = kwargs.get('chatId')
    conversation_id = conversations.get(chatId, '')

    headers = {'Content-Type': 'application/json', }
    # wenxin 只允许发送奇数条数的messages
    if len(messages) % 2 == 0 and len(messages) > 1:
        messages = messages[1:]
    data = json.dumps({
        "messages": messages
    })
    # 如果是检测请求,则直接返回
    msg = messages[-1]
    logger.info(f'baidu-wenxin msg: {msg}')
    if msg['content'] == '你好':
        yield '你好，我是iKnowM。我今天能怎样帮助你？'
        return

    response = requests.post(url + "/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token=" + get_access_token(), headers=headers,
                             data=data, stream=True)
    if not response.ok:
        error_msg = "response is empty"
        logger.info(
            f'baidu-wenxin error: {response.status_code} - {response.reason} - {response.text}')
        yield 'error'

    resps = ['baidu-wenxin==>']
    if response.status_code == 200:
        # for chunk in response.iter_content(chunk_size=128):
        for line in response.iter_lines():
            try:
                line_text = line.decode('utf-8')
                # print(line_text)

                isOk = line_text.find('result":')
                if isOk == -1:
                    logger.error(f'baidu-wenxin error: {line_text}')
                    yield "哎呀，服务开小差了。"
                    continue
                jsonStr = json.loads(line_text)
                answer = jsonStr.get('result', '')
                conversation_id = jsonStr.get('id', '')
                conversations[chatId] = str(conversation_id)

                resps.append(answer)
                yield answer
            except Exception as e:
                # 捕获异常并打印错误信息
                print("发生异常:", str(e))
                logger.error("baidu-wenxin error===>", str(e), exc_info=True)

                # yield line
    respStr = ''.join(resps)
    logger.info(f'baidu-wenxin resp:{respStr}')


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials",
              "client_id": wenxin['api_key'],
              "client_secret": wenxin['secret_key']}

    return str(requests.post(url, params=params).json().get("access_token"))


params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join(
        [f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])
