from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class HuggingfaceBackend:
    def __init__(self, model_name, api_key=None, max_tokens=512, temperature=0):
        self.model_name = model_name
        if api_key is not None:
            self.model = AutoModelForCausalLM.from_pretrained(model_name, token=api_key, device_map="auto", torch_dtype="auto")
        else:
            self.model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", torch_dtype="auto")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.max_tokens = max_tokens
        self.temperature = temperature

        self.device = "cuda" if torch.cuda.is_available() else "cpu"
def chat(self, prompt, system=None):
    message = []

    # Add system message only if 'system' is not None
    if system is not None:
        message.append({
            "role": "system",
            "content": system
        })

    # Add the user message
    message.append({
        "role": "user",
        "content": prompt  # Assuming 'user_content' is the user's input
    })

    message_tokens = self.tokenizer.apply_chat_template(message, add_generation_prompt=True, return_tensors="pt").to("cuda")
    input_length = message_tokens.shape[-1]
    generated_ids = self.model.generate(
        message_tokens,
        temperature=self.temperature,
        max_new_tokens=self.max_tokens,
    )

    response = self.tokenizer.batch_decode(generated_ids[:, input_length:], skip_special_tokens=True)[0]
    return response
