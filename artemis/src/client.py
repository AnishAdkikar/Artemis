from dataclasses import dataclass
from requests import Session

# con = artemis.connect()
# con.add_vector()
# con.query()

def _authenticate(url: str, user: str, password: str) -> bool:
    # authentication_response = request.post(f"{url}/connection", data={"user": user, "password": password})
    # return authentication_response.status_code == 200
    return True


@dataclass
class Connection:
    url: str
    user: str
    password: str

    def __post_init__(self):
        self.session = Session()

        # NEED TO CHANGE THIS IN THE FUTURE TO USE THE ACTUAL DATA
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

    def query(self, query_vector):
        # NEED TO CHANGE THIS IN THE FUTURE TO USE THE ACTUAL DATA
        searchData = {
            'userID':self.user,
            'K':3,
            'ef': 10,
            'data': query_vector
        }

        search_response = self.session.post(url=f'{self.url}/search', json=searchData)
    
        if search_response.status_code != 200:
            raise ValueError("Error while searching")
        return search_response.json()["res"]


def connect(url: str, user: str, password: str) -> Connection:
    if _authenticate(url, user, password):
        conn = Connection(url, user, password)
    else:
        raise ValueError("Authentication failed. Please check your credentials.")

    return conn