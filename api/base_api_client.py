
import requests
import json
from config.config import Config

class BaseApiClient:
    def __init__(self, base_url=Config.API_BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()

    def _send_request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            return response
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error: {e.response.status_code} - {e.response.text}")
            raise
        except requests.exceptions.ConnectionError as e:
            print(f"Connection Error: {e}")
            raise
        except requests.exceptions.Timeout as e:
            print(f"Timeout Error: {e}")
            raise
        except requests.exceptions.RequestException as e:
            print(f"Request Exception: {e}")
            raise

    def get(self, endpoint, params=None, headers=None):
        return self._send_request("GET", endpoint, params=params, headers=headers)

    def post(self, endpoint, data=None, json=None, headers=None):
        return self._send_request("POST", endpoint, data=data, json=json, headers=headers)

    def put(self, endpoint, data=None, json=None, headers=None):
        return self._send_request("PUT", endpoint, data=data, json=json, headers=headers)

    def delete(self, endpoint, headers=None):
        return self._send_request("DELETE", endpoint, headers=headers)

    def patch(self, endpoint, data=None, json=None, headers=None):
        return self._send_request("PATCH", endpoint, data=data, json=json, headers=headers)

    def close_session(self):
        self.session.close()
