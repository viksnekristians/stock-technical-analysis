import requests

class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint: str, params: dict = None, headers: dict = None):
        url = f"{self.base_url}/{endpoint}"
        
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise RuntimeError(f"API Request failed: {e}")