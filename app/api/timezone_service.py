import logging
from app.api.api_client import APIClient

class Timezone:
    def __init__(self, api_client: APIClient):
        self.api_client = api_client

    def get_timezones(self):
        """Mevcut tüm zaman dilimlerini almak için kullanılan metod"""
        endpoint = "timezone"
        logging.info("Mevcut tüm zaman dilimleri alınıyor.")
        return self.api_client.make_request(endpoint)