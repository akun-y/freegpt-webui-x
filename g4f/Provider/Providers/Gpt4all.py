# encoding:utf-8

from requests import Session
from uuid import uuid4
from json import loads
import os
import json
import requests
import gpt4all

from server.logger import init_logger
from ...typing import sha256, Dict, get_type_hints
from gpt4all import GPT4All


url = 'https://gpt-gm.h2o.ai'
model = ['gpt4all-7b']
supports_stream = True
needs_auth = False

models = {
    'Wizard 7B': "wizardLM-13B-Uncensored.ggmlv3.q4_0.bin",
    'Wizard 13B': "wizardlm-13b-v1.1-superhot-8k.ggmlv3.q4_0.bin",
    "Nous-Hermes": "nous-hermes-13b.ggmlv3.q4_0.bin",
    "gpt4all-7b": "ggml-gpt4all-j-v1.3-groovy.bin",
}

# ---------------------------------------------
# gpt4all

logger = init_logger('gpt4all')
config = json.load(open('config.json', 'r'))
model_name = config['gpt4all'].get('model_name')
model_path = config['gpt4all'].get('model_path')
debug = config['debug']

print("gpt4all version:")
print(dir(gpt4all))
print(gpt4all.__name__)
print("gpt4all debug:%s", debug)
# gpt4allModel = GPT4All("wizardlm-13b-v1.1-superhot-8k.ggmlv3.q4_0.bin")
if debug:
    gpt4allModel = GPT4All("ggml-gpt4all-j-v1.3-groovy")
else:
    print("--------")
    print("gpt4all model_name:%s", model_name)
    print("gpt4all model_path:%s", model_path)
    gpt4allModel = GPT4All(model_name=model_name,
                           model_path=model_path, allow_download=False)


# gpt4allModel = GPT4All(
#     model_name="wizardLM-13B-Uncensored.ggmlv3.q4_0",
#     # model_name="orca-mini-13b.ggmlv3.q4_0",
#     # model_name="GPT4All-13B-snoozy.ggmlv3.q4_0",
#     # model_name="nous-hermes-13b.ggmlv3.q4_0",
#     #model_name="ggml-gpt4all-j-v1.3-groovy.bin",
#     # model_name="orca-mini-7b.ggmlv3.q4_0.bin",
#     # model_name='orca-mini-3b.ggmlv3.q4_0.bin',
#     # model_path='/mnt/k/tmp/GPT4All-models',
#     # model_path='/www/cosfs/gpt/models',
#     #model_path='M:\dev\AI\GPT4All-models',
#     model_path='/Users/yhk/.cache/gpt4all',
#     #model_path="gpt4all",
#     allow_download=False)

def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    global logger, gpt4allModel

    logger.info("_create_completion model:%s", model)

    last_item = messages.pop()
    prompt = last_item['content']
    print("gpt4all prompt:", prompt)

    with gpt4allModel.chat_session():
        for message in messages:
            gpt4allModel.current_chat_session.append(
                {'role': message['role'], 'content': message['content']})

        for token in gpt4allModel.generate(prompt, max_tokens=2048, temp=0.7, 
                                           top_k=40, top_p=0.4, repeat_penalty=1.18, repeat_last_n=64, n_batch=8, n_predict=None, streaming=True):
            print(token, end='', flush=True)
            yield (token)

        print("\nResponse: ", json.dumps(
            gpt4allModel.current_chat_session, indent=4, ensure_ascii=False))


params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join(
        [f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])
