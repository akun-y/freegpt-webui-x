import json
from gpt4all import GPT4All
import sys

#model = GPT4All('ggml-mpt-7b-chat')
#model = GPT4All('orca-mini-3b.ggmlv3.q4_0')


model = GPT4All('orca-mini-13b.ggmlv3.q4_0')
#model = GPT4All('gpt4all-lora-quantized')
message = "hello"  # sys.argv[1]
messages = []
print("Prompt: " + message)
messages.append({"role": "user", "content": message})
full_prompt = "sdf"# model._build_prompt(messages, True, True)
response_tokens = []


def test_a():
    global model
    global response_tokens
    # for token in model.generate(full_prompt, streaming=True):
    for token in model.generate("why hair is yellow?", streaming=True):
        response_tokens.append(token)
        # print("token:",token)

    print("Response: " + ''.join(response_tokens))


def test_b():
    global model
    global response_tokens
    response_tokens = []
    messages = [
        {"role": "user", "content": "Can you explain what is a large language model?"}]
    ret = model.chat_completion(messages)

    messages.append(ret["choices"][0]["message"])
    messages.append(
        {"role": "user", "content": "Can you give some examples applications?"})
    ret = model.chat_completion(messages)

    messages.append(ret["choices"][0]["message"])
    messages.append({"role": "user", "content": "Are there any limitations?"})
    ret = model.chat_completion(messages)

    messages.append(ret["choices"][0]["message"])
    messages.append(
        {"role": "user", "content": "Summarize the above in two sentences."})
    ret = model.chat_completion(messages)

    print("-------------------------------1")
    print(json.dumps(messages, indent=4))
    print("-------------------------------2")
    print(json.dumps(ret, indent=4))
    print("-------------------------------3")
# def local_callback(token_id, response):
#     decoded_token = response.decode('utf-8')
#     response_tokens.append( decoded_token );

#     # Do whatever you want with decoded_token here.

#     return True

# model.model._response_callback = local_callback
# model.model.generate(full_prompt, streaming=False)
# response = ''.join(response_tokens)
# print ( "Response: " + response );
# messages.append({"role": "assistant", "content": response});

# At this point, you can get another prompt from the user, re-run "_build_prompt()", and continue the conversation.


test_a()
print("-----------------------------")
test_b()
