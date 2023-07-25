# encoding:utf-8

from requests import Session
from uuid import uuid4
from json import loads
import os
import json
import requests
from ...typing import sha256, Dict, get_type_hints
from gpt4all import GPT4All


url = 'https://gpt-gm.h2o.ai'
model = ['gpt4all-7b']
supports_stream = True
needs_auth = False

models = {
    'gpt4all-7b': 'h2oai/h2ogpt-gm-oasst1-en-2048-falcon-7b-v3',
    'falcon-7b': 'h2oai/h2ogpt-gm-oasst1-en-2048-falcon-7b-v3',
    'falcon-40b': 'h2oai/h2ogpt-gm-oasst1-en-2048-falcon-40b-v1',
    'llama-13b': 'h2oai/h2ogpt-gm-oasst1-en-2048-open-llama-13b'
}

gpt4allModel = GPT4All(
    # model_name="wizardLM-13B-Uncensored.ggmlv3.q4_0",
    # model_name="orca-mini-13b.ggmlv3.q4_0",
    # model_name="GPT4All-13B-snoozy.ggmlv3.q4_0",
    # model_name="nous-hermes-13b.ggmlv3.q4_0",
    model_name="ggml-gpt4all-j-v1.3-groovy.bin",
    # model_name="orca-mini-7b.ggmlv3.q4_0.bin",
    # model_name='orca-mini-3b.ggmlv3.q4_0.bin',
    # model_path='/mnt/k/tmp/GPT4All-models',
    # model_path='/www/cosfs/gpt/models',
    model_path='M:\dev\AI\GPT4All-models',
    allow_download=True)


def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    global gpt4allModel

    prompt = ""
    conversation = []
    for message in messages:
        print("message:", message)
        conversation.append(
            {"role": message['role'], "content": message['content']})
        #prompt += '%s: %s\n' % (message['role'], message['content'])
        prompt = '%s: %s\n' % (message['role'], message['content'])

    print("Prompt: " + prompt)
    # with gpt4allModel.chat_session():
    #     for message in messages:
    #         response = gpt4allModel.generate(prompt=message['content'],  top_k=1)
    #         print("----------------------------")
    #         print(response)
    #         print(gpt4allModel.current_chat_session)

    response_tokens = ''

    # for token in gpt4allModel.generate(prompt,max_tokens=30, streaming=True):
    #     response_tokens.append( token)
    #     print("token:",token)
    for token in gpt4allModel.generate(prompt, max_tokens=30, streaming=True):
        #print("token:", token.encode('utf-8').decode('utf-8'))
        # print(token.decode('utf-8',errors='ignore'))
        response_tokens += token
        yield (token)

    print(response_tokens)
    # print(response_tokens.decode('utf-8',errors='replace'))
    # print("Response: " + response_tokens)
    # conversationId = "234234"

    # if not output or len(output) == 0:
    #     error_msg = "response is empty"
    #     print("conversation completion error:"+error_msg)
    #     error = {'error':error_msg}
    #     yield error
    #     return
    # token  = output;
    # yield token
    # for line in completion.iter_lines():
    #     if b'data' in line:
    #         line = loads(line.decode('utf-8').replace('data:', ''))
    #         token = line['token']['text']

    #         if token == '<|endoftext|>':
    #             break
    #         else:
    #             yield (token)


params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join(
        [f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])
