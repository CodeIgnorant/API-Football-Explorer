import requests
import logging
from app.api.api_connection import APIConnection

class ConnectionTester:
    def __init__(self, api_url, api_key):
        self.api_connection = APIConnection(api_url, api_key)

    def test_connection(self):
        """API bağlantısını test eden metod."""
        try:
            response = requests.get(self.api_connection.api_url, headers=self.api_connection.headers, timeout=10)
            response.raise_for_status()  # Hata durumunda exception fırlatır
            logging.info("API bağlantısı başarılı!")
            return True  # Bağlantı başarılı
        except requests.exceptions.RequestException:
            logging.error("API bağlantısı başarısız!")
            return False  # Bağlantı başarısız