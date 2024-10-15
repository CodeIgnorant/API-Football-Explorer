import requests
import logging
from app.settings.config import Config  # Config'i import et

class APIConnection:
    def __init__(self):
        """
        APIConnection sınıfı, API ile bağlantıyı sağlamak için kullanılır.
        API URL'si ve API anahtarı Config'den alınır.
        """
        self.api_url = Config.api_url  # Config'den API URL'sini al
        self.api_key = Config.api_key  # Config'den API anahtarını al

        # API Key kontrolü ve çıktısı
        if not self.api_key:
            logging.error("API Key bulunamadı. Lütfen doğru API anahtarını sağlayın.")
            raise ValueError("API Key bulunamadı.")
        else:
            logging.info(f"API Key başarıyla alındı: {self.api_key[:4]}****")

        # Headers - API sadece belirli başlıkları kabul eder
        self.headers = {
            "x-apisports-key": self.api_key  # Apisports API key
        }

    def test_connection(self):
        """API bağlantısını test eden metod."""
        try:
            response = requests.get(self.api_url, headers=self.headers, timeout=10)
            response.raise_for_status()  # Hata durumunda exception fırlatır
            logging.info("API bağlantısı başarılı!")  # Başarılı bağlantı logu
            return True  # Bağlantı başarılı
        except requests.exceptions.RequestException as req_err:
            logging.error(f"API bağlantısı başarısız! Hata: {req_err}")
            return False  # Bağlantı başarısız