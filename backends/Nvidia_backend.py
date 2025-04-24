from backends.openai_compatible_backend import GenericOpenAIBackend


class NvidiaBackend(GenericOpenAIBackend):

    def __init__(self, model_name, model_id, api_key, base_url, max_tokens, temperature=0):
        super().__init__(model_name, model_id, api_key, base_url, max_tokens, temperature)
