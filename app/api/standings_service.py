import logging
from app.api.api_client import APIClient

class Standings:
    def __init__(self, api_client: APIClient):
        self.api_client = api_client

    def get_standings_league_season(self, league_id, season):
        """Belirli bir lig ve sezona göre sıralamaları almak için kullanılan metod"""
        endpoint = "standings"
        params = {
            "league": league_id,
            "season": season
        }
        logging.info(f"{league_id} ligindeki {season} sezonunun sıralamaları alınıyor.")
        return self.api_client.make_request(endpoint, params=params)