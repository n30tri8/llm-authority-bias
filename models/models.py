from anthropic import Anthropic


class Claude3(Anthropic):
    def __init__(self, model_name):
        super(Claude3, self).__init__()
        self.model_name = model_name

    def chat(self, prompt, system=None, temperature= 0, max_token=512):
        """ Should be distinguished because the Anthropic API makes a distincition between omitted and None param values, so I cannot just pass None"""
        if system is None:
            message = self.messages.create(
                max_tokens=max_token,
                temperature=temperature,
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
                max_tokens=max_token,
                temperature=temperature,
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

