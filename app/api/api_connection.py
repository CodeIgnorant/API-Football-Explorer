import requests
import logging

class APIConnection:
    def __init__(self, api_url, api_key):
        """
        APIConnection sınıfı, API ile bağlantıyı sağlamak için kullanılır.
        api_url ve api_key parametreleri dışarıdan enjekte edilerek bağımlılıkların gevşek olmasını sağlar.
        """
        self.api_url = api_url
        self.api_key = api_key

        # API Key kontrolü ve çıktısı
        if not self.api_key:
            raise ValueError("API Key bulunamadı. Lütfen doğru API anahtarını sağlayın.")
        else:
            logging.info(f"API Key başarıyla alındı: {self.api_key[:4]}****")

        # Headers - API sadece belirli başlıkları kabul eder
        self.headers = {
            "x-apisports-key": self.api_key  # Apisports API key
        }