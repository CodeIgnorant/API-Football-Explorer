from app.api.api_client import APIClient
import logging

class Leagues:
    def __init__(self, api_client: APIClient):  # APIClient'ı parametre olarak al
        self.api_client = api_client  # APIClient nesnesini al

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

        if response is None or len(response) == 0:
            logging.error("Ligler alınamadı.")
            return None  # Hata durumunda None döndür

        logging.info("Ligler başarıyla alındı.")
        return response  # API yanıtını döndür

    def get_leagues_country_season_type(self, country_name, season, league_type):
        """Belirli bir ülkeye, sezona ve lig türüne göre ligleri almak için kullanılan metod."""
        if not country_name or len(country_name) < 2:
            logging.error("Geçersiz ülke adı. En az 2 karakter olmalıdır.")
            return None  # Hata durumunda None döndür

        if league_type not in ["league", "cup"]:
            logging.error("Geçersiz lig türü. 'league' veya 'cup' olmalıdır.")
            return None  # Hata durumunda None döndür

        endpoint = "leagues"
        params = {
            "country": country_name,
            "season": season,
            "type": league_type
        }
        logging.info(f"{country_name} ülkesindeki {league_type} türündeki ligler alınıyor.")
        response = self.api_client.send_request(endpoint, params=params)

        if response is None or len(response) == 0:
            logging.error("Ligler alınamadı.")
            return None  # Hata durumunda None döndür

        logging.info("Ligler başarıyla alındı.")
        return response  # API yanıtını döndür
