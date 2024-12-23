from base.services.api_client import ApiClient

class AlphavantageApiClient(ApiClient):
    BASE_URL = 'https://www.alphavantage.co'
    API_KEY = 'P50DH8XQ9SKA2ANB'
    TIMEOUT = 30
    MAX_RETRIES = 3

    def __init__(self):
        super().__init__(self.BASE_URL)

    def getDailyInfo(self, symbol: str):
        return self.get('query', {'function': 'TIME_SERIES_DAILY', 'symbol': symbol, 'apikey': self.API_KEY})
