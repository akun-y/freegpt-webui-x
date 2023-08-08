import uuid
import requests
import os
import json
from g4f.utils import Utils

from server.logger import init_logger
from ...typing import sha256, Dict, get_type_hints

# curl --location --request POST 'https://api.dify.ai/v1/chat-messages' \
# --header 'Authorization: Bearer app-11111AszUIqcFIhFlapQ3EpXwV4JJ' \
# --header 'Content-Type: application/json' \
# --data-raw '{
#     "inputs": {},
#     "query": "一年中什么时候最热？",
#     "response_mode": "blocking",
#     "user": "abc-123"
# }'

url = 'https://api.dify.ai'
model = ['gpt-3.5-turbo-16k', 'gpt-3.5-turbo-0613']
supports_stream = True
needs_auth = False
logger = init_logger('dify-ai')


config = json.load(open('config.json', 'r'))
apikey = config['dify_ai_apikey']
conversations = {}
def _create_completion(model: str, messages: list, stream: bool, temperature: float = 0.7, **kwargs):
    global logger,apikey,conversations

    chatId = kwargs.get('chatId')
    conversation_id = conversations.get(chatId,'')

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer app-{apikey}',
    }
    data = {
        "inputs": {},
        "query": messages,
        "response_mode": "streaming",  # "blocking",#streaming
        "user": chatId,
        "conversation_id": conversation_id
    }
    #如果是检测请求,则直接返回
    msg = messages[-1]
    logger.info(f'dify-ai msg: {msg}')
    if msg['content'] == '你好':
        yield '你好，我是iKnowM。我今天能怎样帮助你？'
        return

    response = requests.post(url + '/v1/chat-messages', headers=headers,
                             json=data, stream=True)
    if not response.ok:
        error_msg = "response is empty"
        logger.info(
            f'dify-ai error: {response.status_code} - {response.reason} - {response.text}')

    resps = ['dify-ay::']
    if response.status_code == 200:
        # for chunk in response.iter_content(chunk_size=128):
        for line in response.iter_lines():
            try:
                line_text = line.decode('utf-8')
                # print(line_text)

                data_start = line_text.find('data:')
                if data_start == -1:
                    continue

                data_start = len('data:')
                data_string = line_text[data_start:]

                resp = json.loads(data_string)
                answer = resp.get('answer')
                conversation_id = resp.get('conversation_id')
                conversations[chatId] = str(conversation_id)

                # 'event':'message'
                # 'task_id':'c68363ac-fd2c-45de-8457-626a30b2777c'
                # 'id':'dc6c7616-d384-4662-8bd1-e8aacc95233c'
                # 'answer':''
                # 'created_at':1691457800
                # 'conversation_id':'a0a6554f-e113-4964-bb24-d97560f1b955'

                # print(answer)
                resps.append(answer)
                yield answer
            except Exception as e:
                # 捕获异常并打印错误信息
                print("发生异常:", str(e))
                logger.error("dify-ai error===>", str(e), exc_info=True)

                # yield line
    logger.info(f'dify-ai resp:{resps}')


params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join(
        [f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])
