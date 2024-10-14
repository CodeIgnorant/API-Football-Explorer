import requests
import logging
from app.api.api_connection import APIConnection

class APIClient:
    def __init__(self, api_url, api_key):
        # APIConnection için gerekli parametreleri alıyoruz
        self.api_connection = APIConnection(api_url, api_key)
        self.base_url = self.api_connection.api_url
        self.headers = self.api_connection.headers
        self.timezone = "Europe/Istanbul"  # Saat dilimini sabit olarak belirledik

    def send_request(self, endpoint, params=None):
        """Genel API isteği yapmak için kullanılan metod"""
        url = f"{self.base_url}/{endpoint}"
        logging.info(f"URL oluşturuldu: {url}")  # URL'nin oluşturulduğunu kontrol etmek için log

        # Parametreler None ise boş bir dict oluştur
        params = params or {}

        try:
            response = requests.get(url, headers=self.headers, params=params, timeout=10)
            response.raise_for_status()  # Hata durumunda exception fırlatır
            return response.json()  # API yanıtını doğrudan döndür
        except requests.exceptions.RequestException as e:
            logging.error(f"İstek sırasında hata oluştu: {e}")
            return {"error": "API bağlantısı başarısız oldu"}