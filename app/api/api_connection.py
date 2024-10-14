import requests
import logging

class APIConnection:
    def __init__(self, api_url, api_key, rapidapi_host):
        """
        APIConnection sınıfı, API ile bağlantıyı sağlamak için kullanılır.
        api_url, api_key ve rapidapi_host parametreleri dışarıdan enjekte edilerek bağımlılıkların gevşek olmasını sağlar.
        """
        self.api_url = api_url
        self.api_key = api_key
        self.rapidapi_host = rapidapi_host

        # API Key kontrolü ve çıktısı
        if not self.api_key:
            raise ValueError("API Key bulunamadı. Lütfen doğru API anahtarını sağlayın.")
        else:
            logging.info(f"API Key başarıyla alındı: {self.api_key[:4]}****")

        # Headers - API sadece belirli başlıkları kabul eder
        self.headers = {
            "x-rapidapi-host": self.rapidapi_host,  # API sağlayıcısının beklediği host header'ı
            "x-rapidapi-key": self.api_key,         # API key
            "x-apisports-key": self.api_key         # Apisports API key (aynı anahtarı kullanıyor olabilir)
        }

    def test_connection(self):
        """API'ye bağlantı kurup kuramadığımızı test eder."""
        try:
            response = requests.get(self.api_url, headers=self.headers, timeout=10)
            if response.status_code == 200:
                logging.info("API bağlantısı başarılı!")
                return True
            else:
                logging.error(f"API bağlantısı başarısız! Status code: {response.status_code}")
                return False
        except requests.exceptions.RequestException as e:
            logging.error(f"API bağlantısı sırasında hata oluştu: {e}")
            return False
