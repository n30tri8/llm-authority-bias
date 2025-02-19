from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class HuggingfaceBackend:
    def __init__(self, model_name, model_id, api_key=None, max_tokens=512, temperature=0.0):
        self.model_name = model_name
        self.model_id = model_id
        if api_key is not None:
            self.model = AutoModelForCausalLM.from_pretrained(model_id, token=api_key, device_map="auto", torch_dtype="auto")
            self.tokenizer = AutoTokenizer.from_pretrained(model_id, token=api_key)
        else:
            self.model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto", torch_dtype="auto")
            self.tokenizer = AutoTokenizer.from_pretrained(model_id)

        self.max_tokens = max_tokens
        self.temperature = temperature
        # check if model's generation_config has pad_token_id set:
        if not self.model.generation_config.pad_token_id:
            # set pad_token_id to tokenizer's eos_token_id to prevent excessive warnings:
            self.model.generation_config.pad_token_id = self.tokenizer.eos_token_id

        self.device = "cuda" if torch.cuda.is_available() else "cpu"
    def chat(self, prompt):
        message_tokens = self.tokenizer.apply_chat_template(prompt, add_generation_prompt=True, return_tensors="pt").to("cuda")
        input_length = message_tokens.shape[-1]
        generated_ids = self.model.generate(
            message_tokens,
            max_new_tokens=self.max_tokens,
            do_sample=False,
            top_p = None,
            temperature = None
        )

        response = self.tokenizer.batch_decode(generated_ids[:, input_length:], skip_special_tokens=True)[0]
        return response
