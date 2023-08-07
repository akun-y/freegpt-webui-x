import requests
import os
import json

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


def _create_completion(model: str, messages: list, stream: bool, temperature: float = 0.7, **kwargs):
    global logger
    config = json.load(open('config.json', 'r'))
    apikey = config['dify_ai_apikey']

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer app-{apikey}',
    }
    data = {
        "inputs": {},
        "query": messages,
        "response_mode": "streaming",  # "blocking",#streaming
        "user": "abc-123",
        "conversation_id": ""
    }
    response = requests.post(url + '/v1/chat-messages', headers=headers,
                             json=data, stream=True)
    if not response.ok:
        error_msg = "response is empty"
        logger.info(
        f'dify-ai error: {response.status_code} - {response.reason} - {response.text}')

    resps = ['dify-ay::']
    if response.status_code == 200:
        #for chunk in response.iter_content(chunk_size=128):
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
                #print(answer)
                resps.append(answer)
                yield answer
            except:
                print('error')

                # yield line
    logger.info(f'dify-ai resp:{resps}')
params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join(
        [f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])
