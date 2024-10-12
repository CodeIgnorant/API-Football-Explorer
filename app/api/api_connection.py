import requests
import logging
from app.settings.config import Config

class APIConnection:
    def __init__(self):
        config = Config()
        self.api_url = config.api_url
        self.api_key = config.api_key

        # API Key kontrolü ve çıktısı
        if not self.api_key:
            raise ValueError("API Key bulunamadı. Lütfen ortam değişkenlerini kontrol edin.")
        else:
            logging.info(f"API Key başarıyla alındı: {self.api_key[:4]}****")

        # Header'ı doğru şekilde yapılandıralım
        self.headers = {
            "x-rapidapi-key": self.api_key  # API sağlayıcısının beklediği header formatı
        }

    def test_connection(self):
        """API'ye bağlantı kurup kuramadığımızı test eder."""
        try:
            response = requests.get(self.api_url, headers=self.headers)
            if response.status_code == 200:
                logging.info("API bağlantısı başarılı!")
                return True
            else:
                logging.error(f"API bağlantısı başarısız! Status code: {response.status_code}")
                return False
        except requests.exceptions.RequestException as e:
            logging.error(f"API bağlantısı sırasında hata oluştu: {e}")
            return False