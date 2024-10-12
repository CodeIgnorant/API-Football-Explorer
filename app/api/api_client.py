import requests
import logging
from app.settings.config import Config

class APIConnection:
    def __init__(self):
        config = Config()
        self.api_url = config.api_url
        self.api_key = config.api_key

        # Header yapısını API sağlayıcısının beklediği şekilde ayarladık.
        self.headers = {
            "x-rapidapi-key": self.api_key
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


class APIClient:
    def __init__(self):
        # API bağlantısını kontrol etmek için APIConnection kullanılır
        self.api_connection = APIConnection()
        if not self.api_connection.test_connection():
            raise ConnectionError("API bağlantısı kurulamadı. Lütfen API URL ve anahtarını kontrol edin.")
        
        self.base_url = self.api_connection.api_url
        self.headers = self.api_connection.headers
        self.timezone = "Europe/Istanbul"  # Saat dilimini sabit olarak belirledik

    def make_request(self, endpoint, params=None, retries=3):
        """Genel API isteği yapmak için kullanılan metod"""
        url = f"{self.base_url}/{endpoint}"
        logging.info(f"URL oluşturuldu: {url}")  # URL'nin oluşturulduğunu kontrol etmek için log

        # Parametreler None ise boş bir dict oluştur
        if params is None:
            params = {}

        for attempt in range(retries):
            try:
                response = requests.get(url, headers=self.headers, params=params, timeout=10)
                logging.info(f"API'ye istek gönderildi: Deneme {attempt + 1}")  # İstek gönderildiğini kontrol etmek için log
                logging.info(f"Yanıt Durum Kodu: {response.status_code}")  # Yanıt durum kodunu kontrol etmek için log
                response.raise_for_status()
                logging.info(f"Yanıt İçeriği: {response.text}")  # Yanıtın tüm içeriğini loglayalım
                return self.extract_response(response.json())
            except requests.exceptions.RequestException as e:
                logging.error(f"İstek sırasında hata oluştu: {e} - Deneme: {attempt + 1}")

                if attempt < retries - 1:
                    logging.info("Tekrar deneniyor...")
                else:
                    logging.error("Tüm denemeler başarısız oldu.")
                    return {"error": "API bağlantısı başarısız oldu", "status": response.status_code if response else "No response"}

    def extract_response(self, response):
        """API yanıtını esnek bir şekilde işleyen metod"""
        if isinstance(response, dict) and "response" in response:
            # Yanıt bir sözlükse ve 'response' anahtarını içeriyorsa bunu döndürelim
            return response["response"]
        elif isinstance(response, list):
            # Eğer yanıt bir listeyse direkt olarak listeyi döndürelim
            return response
        else:
            # Beklenmeyen bir yapı dönerse bir hata logu verelim
            logging.error("Beklenen veri yapısı bulunamadı.")
            logging.error(f"Tam Yanıt: {response}")  # Yanıtı daha detaylı görmek için tam içeriği log
            return None
