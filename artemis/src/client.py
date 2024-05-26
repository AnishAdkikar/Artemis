from dataclasses import dataclass
from joblib import Parallel, delayed
import requests

@dataclass
class VectorDb:
    user: str
    password: str
    url: str = "http://127.0.0.1:8080"
    threads: int = 10

    def __post_init__(self):
        self.session = requests.Session()
        userData = {
            'userID': self.user,
            'M': str(10),
            'efConstruction': str(20)
        }
        con_request = self.session.post(url=f"{self.url}/connection", json=userData)
        if con_request.status_code != 200:
            self.session.close()
            raise ValueError("Connection Error")

    def add_vector(self, vector: dict):
        addData = {
            'userID': self.user,
            'data': vector
        }
        add_data_response = self.session.post(f"{self.url}/add-data", json=addData)
        if add_data_response.status_code != 200:
            raise ValueError("Error while adding")
        
    def convert_to_vectors(self,multi_func,texts):
        results = Parallel(n_jobs=min(self.threads, len(texts)))(delayed(multi_func)(text) for text in texts)
        vectors = {text: vector for text, vector in results if vector is not None}
        return vectors

    def query(self, query_vector):
        searchData = {
            'userID':self.user,
            'K':3,
            'ef': 10,
            'data': query_vector
        }
        search_response = self.session.post(url=f'{self.url}/search', json=searchData)
        if search_response.status_code != 200:
            raise ValueError("Error while searching")
        return search_response.json()