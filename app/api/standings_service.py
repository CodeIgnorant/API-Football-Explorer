import logging
from app.api.api_client import APIClient

class Standings:
    def __init__(self, api_client: APIClient):
        self.api_client = api_client

    def get_standings_league_season(self, league_id, season):
        """Method used to retrieve standings based on a specific league and season."""
        if not isinstance(league_id, int) or league_id <= 0:
            logging.error("Invalid league ID. It must be a positive integer.")
            return None  # Return None in case of error

        if not isinstance(season, int) or not (1000 <= season <= 9999):
            logging.error("Invalid season. It must be in year format (YYYY).")
            return None  # Return None in case of error

        endpoint = "standings"
        params = {
            "league": league_id,
            "season": season
        }
        logging.info(f"Retrieving standings for league {league_id} for the {season} season.")
        
        # Send request with APIClient
        response = self.api_client.send_request(endpoint, **params)

        if response and "error" in response:
            logging.error(f"Standings could not be retrieved for league {league_id} for the {season} season.")
            return None  # Return None in case of error

        logging.info(f"Standings for league {league_id} for the {season} season successfully retrieved.")
        return response