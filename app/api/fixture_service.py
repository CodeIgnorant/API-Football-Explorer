import logging
from datetime import datetime, timedelta
from app.api.api_client import APIClient

class Fixtures:
    def __init__(self, api_client: APIClient):
        self.api_client = api_client

    def get_fixture_id(self, fixture_id):
        """Belirli bir maç ID'sine göre maç bilgilerini almak için kullanılan metod"""
        endpoint = "fixtures"
        params = {"id": fixture_id}
        logging.info(f"Fixture ID'si ile maç bilgileri alınıyor: {fixture_id}")
        return self.api_client.make_request(endpoint, params=params)

    def get_fixtures_league_season(self, league_id, season, status=None):
        """Belirli bir lig, sezon ve opsiyonel olarak duruma göre maçları almak için kullanılan metod"""
        endpoint = "fixtures"
        params = {
            "league": league_id,
            "season": season
        }
        if status:
            params["status"] = status
        logging.info(f"Lig {league_id} ve sezon {season} için maçlar alınıyor.")
        return self.api_client.make_request(endpoint, params=params)

    def get_fixtures_team_league_season(self, team_id, league_id, season, status=None):
        """Belirli bir takımın, lig ve sezondaki maçlarını almak için kullanılan metod"""
        endpoint = "fixtures"
        params = {
            "team": team_id,
            "league": league_id,
            "season": season
        }
        if status:
            params["status"] = status
        logging.info(f"Takım {team_id}, lig {league_id} ve sezon {season} için maçlar alınıyor.")
        return self.api_client.make_request(endpoint, params=params)

    def get_upcoming_fixtures_league_season(self, league_id, season):
        """Belirli bir lig ve sezonda, bugünden itibaren 3 gün boyunca NS durumundaki maçları almak için kullanılan metod"""
        endpoint = "fixtures"
        today = datetime.today().strftime('%Y-%m-%d')
        three_days_later = (datetime.today() + timedelta(days=3)).strftime('%Y-%m-%d')
        params = {
            "league": league_id,
            "season": season,
            "status": "NS",
            "from": today,
            "to": three_days_later
        }
        logging.info(f"Lig {league_id} ve sezon {season} için yaklaşan maçlar alınıyor. Tarih aralığı: {today} - {three_days_later}")
        return self.api_client.make_request(endpoint, params=params)