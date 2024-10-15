import logging
from app.api.api_client import APIClient

class Leagues:
    def __init__(self):
        # APIClient'ı Config'den al
        self.api_client = APIClient()

    def get_leagues_country_current_type(self, country_name, league_type):
        """Belirli bir ülkeye, aktif sezona ve lig türüne göre ligleri almak için kullanılan metod."""
        if not country_name or len(country_name) < 2:
            logging.error("Geçersiz ülke adı. En az 2 karakter olmalıdır.")
            return None  # Hata durumunda None döndür

        if league_type not in ["league", "cup"]:
            logging.error("Geçersiz lig türü. 'league' veya 'cup' olmalıdır.")
            return None  # Hata durumunda None döndür

        endpoint = "leagues"
        params = {
            "country": country_name,
            "type": league_type,
            "current": "true"
        }
        logging.info(f"{country_name} ülkesindeki {league_type} türündeki aktif ligler alınıyor.")
        response = self.api_client.send_request(endpoint, params=params)

        if isinstance(response, dict) and "error" in response:
            logging.error(f"{country_name} ülkesindeki ligler alınamadı.")
            return None  # Hata durumunda None döndür

        logging.info(f"{country_name} ülkesindeki {league_type} türündeki ligler başarıyla alındı.")
        return response

    def get_leagues_type(self, league_type):
        """Lig türüne göre ligleri almak için kullanılan metod (league veya cup)."""
        if league_type not in ["league", "cup"]:
            logging.error("Geçersiz lig türü. 'league' veya 'cup' olmalıdır.")
            return None  # Hata durumunda None döndür

        endpoint = "leagues"
        params = {
            "type": league_type
        }
        logging.info(f"{league_type} türündeki ligler alınıyor.")
        response = self.api_client.send_request(endpoint, params=params)

        if isinstance(response, dict) and "error" in response:
            logging.error(f"{league_type} türündeki ligler alınamadı.")
            return None  # Hata durumunda None döndür

        logging.info(f"{league_type} türündeki ligler başarıyla alındı.")
        return response