import logging
from app.api.api_client import APIClient

class Leagues:
    def __init__(self, api_client: APIClient):
        self.api_client = api_client

    def get_leagues_country_current_type(self, country_name, league_type):
        """Belirli bir ülkeye, aktif sezona ve lig türüne göre ligleri almak için kullanılan metod"""
        endpoint = "leagues"
        params = {
            "country": country_name,
            "current": "true",
            "type": league_type
        }
        logging.info(f"{country_name} ülkesindeki {league_type} türündeki aktif ligler alınıyor.")
        return self.api_client.make_request(endpoint, params=params)

    def get_leagues_type(self, league_type):
        """Lig türüne göre ligleri almak için kullanılan metod (league veya cup)"""
        endpoint = "leagues"
        params = {
            "type": league_type
        }
        logging.info(f"{league_type} türündeki ligler alınıyor.")
        return self.api_client.make_request(endpoint, params=params)

    def get_leagues_season_type(self, season, league_type):
        """Belirli bir sezona ve lig türüne göre ligleri almak için kullanılan metod"""
        endpoint = "leagues"
        params = {
            "season": season,
            "type": league_type
        }
        logging.info(f"{season} sezonundaki {league_type} türündeki ligler alınıyor.")
        return self.api_client.make_request(endpoint, params=params)

    def get_leagues_country_season_type(self, country_name, season, league_type):
        """Belirli bir ülke, sezon ve lig türüne göre ligleri almak için kullanılan metod"""
        endpoint = "leagues"
        params = {
            "country": country_name,
            "season": season,
            "type": league_type
        }
        logging.info(f"{country_name} ülkesindeki {season} sezonundaki {league_type} ligleri alınıyor.")
        return self.api_client.make_request(endpoint, params=params)