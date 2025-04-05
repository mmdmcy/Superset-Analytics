from requests import Session

class APIConnector:
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.session = Session()
        if headers:
            self.session.headers.update(headers)

    def get(self, endpoint, params=None):
        response = self.session.get(f"{self.base_url}/{endpoint}", params=params)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint, data=None):
        response = self.session.post(f"{self.base_url}/{endpoint}", json=data)
        response.raise_for_status()
        return response.json()

    def put(self, endpoint, data=None):
        response = self.session.put(f"{self.base_url}/{endpoint}", json=data)
        response.raise_for_status()
        return response.json()

    def delete(self, endpoint):
        response = self.session.delete(f"{self.base_url}/{endpoint}")
        response.raise_for_status()
        return response.status_code