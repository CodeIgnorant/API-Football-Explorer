from app.api.api_client import APIClient
import logging

class Leagues:
    def __init__(self, api_client: APIClient):
        self.api_client = api_client

    def get_leagues_country_current_type(self, country_name, league_type):
        if not country_name or len(country_name) < 2:
            logging.error("Geçersiz ülke adı. En az 2 karakter olmalıdır.")
            return None

        if league_type not in ["league", "cup"]:
            logging.error("Geçersiz lig türü. 'league' veya 'cup' olmalıdır.")
            return None

        endpoint = "leagues"
        params = {
            "country": country_name,
            "type": league_type,
            "current": "true"
        }
        logging.info(f"{country_name} ülkesindeki {league_type} türündeki aktif ligler alınıyor.")
        response = self.api_client.send_request(endpoint, params=params)

        if response is None or 'response' not in response or len(response['response']) == 0:
            logging.error("Ligler alınamadı veya API yanıtında beklenmeyen yapı: %s", response)
            return None

        logging.info("Ligler başarıyla alındı.")
        return response['response']

    def get_leagues_country_season_type(self, country_name, season, league_type):
        if not country_name or len(country_name) < 2:
            logging.error("Geçersiz ülke adı. En az 2 karakter olmalıdır.")
            return None

        if league_type not in ["league", "cup"]:
            logging.error("Geçersiz lig türü. 'league' veya 'cup' olmalıdır.")
            return None

        endpoint = "leagues"
        params = {
            "country": country_name,
            "season": season,
            "type": league_type
        }
        logging.info(f"{country_name} ülkesindeki {league_type} türündeki ligler alınıyor.")
        response = self.api_client.send_request(endpoint, params=params)

        if response is None or 'response' not in response or len(response['response']) == 0:
            logging.error("Ligler alınamadı veya API yanıtında beklenmeyen yapı: %s", response)
            return None

        logging.info("Ligler başarıyla alındı.")
        return response['response']
