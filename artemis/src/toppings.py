from abc import ABC, abstractmethod
import requests
from src.config import API_TOKEN

class Topping(ABC):
    def __init__(self, url):
        self.url = url

    @abstractmethod
    def request(self):
        pass

class OpenAITopping(Topping):
    def __init__(self):
        # super().__init__(url)
        self.url = "https://api.openai.com/v1/embeddings"

    def request(self, text):
        header={'Content-Type': 'application/json', 'Authorization': API_TOKEN}
        payload = {
            "model":"text-embedding-3-large",
            "input":text
            }
        response = requests.post(url=self.url, json=payload ,headers=header)
        if response.status_code == 200:
            vector = response.json()["data"][0]["embedding"]
            return text, vector
        return text, None