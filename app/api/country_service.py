import logging
from app.api.api_client import APIClient

class Countries:
    def __init__(self, api_client: APIClient):
        self.api_client = api_client  # APIClient nesnesini al

    def get_all_countries(self):
        """Mevcut tüm ülkelerin listesini almak için kullanılan metod"""
        endpoint = "countries"
        response = self.api_client.send_request(endpoint)  # APIClient ile istek gönder
        logging.info(f"API'den gelen yanıt: {response}")  # Log ekleyelim

        if "error" in response:
            logging.error("API'den hata alındı.")
            return None  # Hata durumunda None döndür

        return response  # API yanıtını döndür

    def get_country_by_name(self, name):
        """Ülke ismine göre ülke bilgilerini almak için kullanılan metod"""
        endpoint = "countries"
        params = {"name": name}
        response = self.api_client.send_request(endpoint, params=params)  # APIClient ile istek gönder

        if "error" in response:
            logging.error(f"{name} ülkesinin bilgileri alınamadı.")
            return None  # Hata durumunda None döndür

        return response  # API yanıtını döndür

    def get_country_by_code(self, code):
        """Ülke koduna göre ülke bilgilerini almak için kullanılan metod"""
        endpoint = "countries"
        params = {"code": code}
        response = self.api_client.send_request(endpoint, params=params)  # APIClient ile istek gönder

        if "error" in response:
            logging.error(f"{code} kodlu ülkenin bilgileri alınamadı.")
            return None  # Hata durumunda None döndür

        return response  # API yanıtını döndür

    def get_country_flag_url(self, country_code):
        """Ülke koduna göre bayrak URL'sini almak için kullanılan metod"""
        return f"https://media.api-sports.io/flags/{country_code}.svg"
