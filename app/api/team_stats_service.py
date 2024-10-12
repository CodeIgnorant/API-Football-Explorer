import logging
from app.api.api_client import APIClient

class TeamStats:
    def __init__(self, api_client: APIClient):
        self.api_client = api_client

    def get_team_statistics(self, team_id, league_id, season, date=None):
        """Belirli bir takımın, lig ve sezondaki istatistiklerini almak için kullanılan metod"""
        endpoint = "teams/statistics"
        params = {
            "team": team_id,
            "league": league_id,
            "season": season
        }
        if date:
            params["date"] = date
        logging.info(f"Takım {team_id}, lig {league_id}, sezon {season} için istatistikler alınıyor.")
        return self.api_client.make_request(endpoint, params=params)
