from huggingface_hub import InferenceClient


class HuggingfaceServerlessBackend:
    def __init__(self, model_name, model_id, provider, api_key=None, max_tokens=512, temperature=0.0):
        self.client = InferenceClient(provider=provider, api_key=api_key, model=model_id)
        self.model_name = model_name
        self.max_tokens = max_tokens
        self.temperature = temperature

    def chat(self, prompt):
        if self.model_name == "DeepSeek-V3-0324-Hugging-Serverless":
            messages = prompt
        else:
            messages = [{"role": "user", "content": prompt}]
        output = self.client.chat_completion(messages, max_tokens=self.max_tokens, stream=False,
                                             temperature=self.temperature)

        parsed_output = output.choices[0].message.content

        return parsed_output
