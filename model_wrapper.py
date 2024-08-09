# model_wrapper.py
from transformers import pipeline

class ModelWrapper:
    def __init__(self, model_name="gpt-2"):
        self.generator = pipeline('text-generation', model=model_name)

    def generate_text(self, prompt, max_length=50):
        return self.generator(prompt, max_length=max_length, num_return_sequences=1)[0]['generated_text']
