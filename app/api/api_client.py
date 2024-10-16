import requests
import logging
from app.api.api_connection import APIConnection

class APIClient:
    def __init__(self):
        # APIConnection'ı oluştur
        self.api_connection = APIConnection()  # Config'den değer almasına gerek yok
        self.base_url = self.api_connection.api_url
        self.headers = self.api_connection.headers
        self.timezone = "Europe/Istanbul"  # Saat dilimini sabit olarak belirledik

    def send_request(self, endpoint, params=None):
        """Genel API isteği yapmak için kullanılan metod.
        Yanıtın her zaman bir liste döneceği varsayılmaktadır.
        """
        url = f"{self.base_url}/{endpoint}"
        logging.info(f"URL oluşturuldu: {url}")

        params = params or {}
        try:
            response = requests.get(url, headers=self.headers, params=params, timeout=10)
            response.raise_for_status()  # HTTP hatalarını kontrol et
            logging.info("API isteği başarılı!")

            return response.json()  # JSON formatında döndür
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP hata oluştu: {http_err}")
        except requests.exceptions.RequestException as req_err:
            logging.error(f"API isteği sırasında hata oluştu: {req_err}")

        return {"error": "API isteği başarısız oldu."}  # Başarısız durumda hata mesajı döner