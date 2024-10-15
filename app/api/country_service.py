import logging
from app.api.api_client import APIClient

class Countries:
    def __init__(self, api_client):  # APIClient'ı parametre olarak al
        self.api_client = api_client  # APIClient nesnesini al

    def get_countries(self):
        """Mevcut tüm ülkelerin listesini almak için kullanılan metod."""
        endpoint = "countries"
        response = self.api_client.send_request(endpoint)  # APIClient ile istek gönder
        logging.debug(f"API'den gelen yanıt: {response}")  # Daha düşük seviye bir log

        if response is None or len(response) == 0:
            logging.error("API'den hata alındı veya yanıt boş.")
            return None  # Hata durumunda None döndür

        logging.info("Tüm ülkeler başarıyla alındı.")
        return response  # API yanıtını döndür

    def get_country_by_name(self, name):
        """Ülke ismine göre ülke bilgilerini almak için kullanılan metod."""
        if len(name) < 3:
            logging.error("Ülke adı en az 3 karakter olmalıdır.")
            return None  # Hata durumunda None döndür

        endpoint = "countries"
        params = {"name": name}
        response = self.api_client.send_request(endpoint, params=params)  # APIClient ile istek gönder

        if response is None or len(response) == 0:
            logging.error(f"{name} ülkesine ait bilgi alınamadı.")
            return None  # Hata durumunda None döndür

        logging.info(f"{name} ülkesinin bilgileri başarıyla alındı.")
        return response  # API yanıtını döndür

    def get_country_by_code(self, code):
        """Ülke koduna göre ülke bilgilerini almak için kullanılan metod."""
        if len(code) < 2 or len(code) > 6:
            logging.error("Ülke kodu 2 ila 6 karakter arasında olmalıdır.")
            return None  # Hata durumunda None döndür

        endpoint = "countries"
        params = {"code": code}
        response = self.api_client.send_request(endpoint, params=params)  # APIClient ile istek gönder

        if response is None or len(response) == 0:
            logging.error(f"{code} ülkesine ait bilgi alınamadı.")
            return None  # Hata durumunda None döndür

        logging.info(f"{code} ülkesinin bilgileri başarıyla alındı.")
        return response  # API yanıtını döndür