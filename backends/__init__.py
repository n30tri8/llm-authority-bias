from backends.anthropic_backend import AnthropicBackend
from backends.huggingface_backend import HuggingfaceBackend
def get_model(model_name, backend, max_tokens = 512):
    if(backend == "huggingface"):
        model = HuggingfaceBackend(model_name, max_tokens)
    elif(backend == "anthropic"):
        model = AnthropicBackend(model_name, max_tokens)
    return model