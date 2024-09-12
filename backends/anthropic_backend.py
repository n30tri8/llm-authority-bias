from anthropic import Anthropic


class AnthropicBackend(Anthropic):
    def __init__(self, model_name, api_key, max_tokens=512):
        super(AnthropicBackend, self).__init__(api_key=api_key)
        self.model_name = model_name
        self.max_tokens = max_tokens
        self.temperature = 0

    def chat(self, prompt, system=None):
        if system is None:
            message = self.messages.create(
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model=self.model_name,
            )
        else:
            message = self.messages.create(
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                system=system,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model=self.model_name,
            )
        return message.content[0].text