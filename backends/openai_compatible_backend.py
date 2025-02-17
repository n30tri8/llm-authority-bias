import openai
import httpx


class GenericOpenAIBackend:

    def __init__(self, model_name, model_id, api_key, base_url, max_tokens, temperature=0):
        self.client = openai.OpenAI(
            base_url=base_url,
            api_key=api_key,
            http_client=httpx.Client(verify=False)
        )
        self.model_name = model_name
        self.model_id = model_id
        self.max_tokens = max_tokens
        self.temperature = temperature

    def chat(self, prompt, system=None):
        """messages = []

        # Add system message only if 'system' is not None
        if system is not None:
            messages.append({
                "role": "system",
                "content": system
            })

        # Add the user message
        messages.append({
            "role": "user",
            "content": prompt  # Assuming 'user_content' is the user's input
        })"""
        print(prompt)
        api_response = self.client.chat.completions.create(model=self.model_id, messages=prompt,
                                                           temperature=self.temperature,
                                                           max_tokens=self.max_tokens)
        message = api_response.choices[0].message.content

        return message

