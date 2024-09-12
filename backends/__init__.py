import json

from backends.anthropic_backend import AnthropicBackend
from backends.huggingface_backend import HuggingfaceBackend
def get_model(model_dict):
    model_name = model_dict['name']
    backend = model_dict['backend']
    gated = True if "gated" in model_dict else False
    max_tokens = model_dict['max_tokens']
    if(backend == "huggingface"):
        model = HuggingfaceBackend(model_name, max_tokens, gated=gated)
    elif(backend == "anthropic"):
        model = AnthropicBackend(model_name, max_tokens)
    return model

def get_credentials(backend):
    credentials_file = "../keys.json"
    credentials = json.load(open(credentials_file))
    return credentials[backend]
