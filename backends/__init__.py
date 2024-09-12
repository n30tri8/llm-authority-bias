import json

from backends.anthropic_backend import AnthropicBackend
from backends.huggingface_backend import HuggingfaceBackend
def get_model(model_dict):
    model_name = model_dict['model_name']
    backend = model_dict['backend']
    gated = True if "gated" in model_dict else False
    max_tokens = model_dict['max_tokens']
    if(backend == "huggingface"):
        api_key = get_credentials(backend) if gated else None
        model = HuggingfaceBackend(model_name, max_tokens=max_tokens, api_key=api_key)
    elif(backend == "anthropic"):
        model = AnthropicBackend(model_name, max_tokens=max_tokens, api_key=get_credentials(backend))
    return model


def get_credentials(backend):
    credentials_file = "../keys.json"
    credentials = json.load(open(credentials_file))
    return credentials[backend]
