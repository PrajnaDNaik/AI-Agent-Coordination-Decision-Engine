import requests


class APIConnector:
    def fetch_api_data(self, url):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return f"API Error: {e}"