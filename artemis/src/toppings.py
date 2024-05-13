from abc import ABC, abstractmethod
import requests
from config import API_TOKEN

class Topping(ABC):
    def __init__(self, url):
        self.url = url

    @abstractmethod
    def request(self):
        pass


class OpenAITopping(Topping):
    def __init__(self, url):
        super().__init__(url)

    def request(self, query):
        header={'Content-Type': 'application/json', 'Authorization': API_TOKEN}
        payload = {
            "model":"text-embedding-3-large",
            "input":query
            }
        
        response = requests.post(url=self.url, json=payload ,headers=header)
        return response