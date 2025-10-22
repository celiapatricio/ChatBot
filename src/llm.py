from openai import OpenAI
from src.config import load_api_key

class LLM:
    def __init__(self):
        self._api_key = load_api_key()
        self.client = OpenAI(api_key=self._api_key,
                             base_url="https://llmproxy.ai.orange")

    def call(self, system_msg: str, user_msg: str) -> str:
        response = self.client.chat.completions.create(
            model="openai/gpt-4.1-nano",
            messages=[
                {
                    "role": "system", 
                    "content": system_msg
                },
                {
                    "role": "user", 
                    "content": user_msg
                }
            ]
        )
        return response.choices[0].message.content

    def get_embedding(self, text: str) -> str:
        """Genera un embedding para el texto dado."""
        response = self.client.embeddings.create(
            model="openai/text-embedding-3-small",
            input=text
        )
        return response.data[0].embedding
    
