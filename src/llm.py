from openai import OpenAI
from src.config import load_api_key

class LLM:
    def __init__(self):
        self._api_key = load_api_key()
        self.client = OpenAI(api_key=self._api_key,
                             base_url="https://llmproxy.ai.orange")
        
    def call(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model="openai/gpt-4.1-nano",
            messages=[
                {
                    "role": "system", 
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user", 
                    "content": prompt
                }
            ]
        )
        return response.choices[0].message.content
