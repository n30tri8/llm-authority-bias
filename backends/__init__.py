import json
from pathlib import Path
from typing import Dict, Union

from backends.Nvidia_backend import NvidiaBackend
from backends.anthropic_backend import AnthropicBackend
from backends.huggingface_backend import HuggingfaceBackend
from backends.huggingface_serverless_backend import HuggingfaceServerlessBackend
from backends.togetherAI_backend import TogetherAIBackend

PROJECT_ROOT = Path(__file__).resolve().parent.parent
def get_model(model_dict: Dict[str, Union[str, bool]], gen_args: Dict[str, Union[int, float]]):
    model_id = model_dict['model_id']
    model_name = model_dict['model_name']
    backend = model_dict['backend']
    gated = True if "gated" in model_dict else False
    max_tokens = gen_args['max_tokens']
    if(backend == "huggingface"):
        api_key = get_credentials(backend)['api_key'] if gated else None
        model = HuggingfaceBackend(model_name, model_id, max_tokens=max_tokens, api_key=api_key)
    elif (backend == "huggingface_serverless"):
        provider = model_dict['provider']
        model = HuggingfaceServerlessBackend(model_name, model_id, max_tokens=max_tokens, provider=provider, api_key=get_credentials(backend)['api_key'])
    elif(backend == "anthropic"):
        model = AnthropicBackend(model_id, max_tokens=max_tokens, api_key=get_credentials(backend)['api_key'])
    elif (backend == "togetherAI"):
        model = TogetherAIBackend(model_name, model_id, max_tokens=max_tokens,
                                  api_key=get_credentials(backend)['api_key'],
                                  base_url=get_credentials(backend)['base_url'])
    elif (backend == "nvidia"):
        model = NvidiaBackend(model_name, model_id, max_tokens=max_tokens,
                                  api_key=get_credentials(backend)['api_key'],
                                  base_url=get_credentials(backend)['base_url'])
    # elif(backend == "openai_compatible"):
    #     model = GenericOpenAIBackend(model_name, model_id, max_tokens=max_tokens, api_key=get_credentials(backend)['api_key'], base_url=get_credentials(backend)['base_url'])
    return model


def get_credentials(backend):
    credentials_file = PROJECT_ROOT / "keys.json"
    credentials = json.load(open(credentials_file))
    return credentials[backend]
