import logging
from datetime import datetime
from app.api.api_client import APIClient

class Fixtures:
    def __init__(self, api_client: APIClient):
        self.api_client = api_client

    def get_fixture_id(self, fixture_id):
        """Method used to retrieve match information based on a specific match ID."""
        if not isinstance(fixture_id, int) or fixture_id <= 0:
            logging.error("Invalid fixture ID. It must be a positive integer.")
            return None  # Return None in case of error

        endpoint = "fixtures"
        params = {"id": fixture_id}
        logging.info(f"Retrieving match information with fixture ID: {fixture_id}")
        response = self.api_client.send_request(endpoint, params=params)

        if response and "error" in response:
            logging.error("Match information could not be retrieved.")
            return None  # Return None in case of error

        logging.info(f"Match information for fixture ID {fixture_id} successfully retrieved.")
        return response

    def get_fixtures_league_season(self, league_id, season, status=None, date=None):
        """Method used to retrieve matches based on a specific league, season, and optionally status."""
        if not isinstance(league_id, int) or league_id <= 0:
            logging.error("Invalid league ID. It must be a positive integer.")
            return None  # Return None in case of error

        if not isinstance(season, int) or not (1000 <= season <= 9999):
            logging.error("Invalid season. It must be in year format (YYYY).")
            return None  # Return None in case of error

        endpoint = "fixtures"
        params = {
            "league": league_id,
            "season": season
        }
        if status:
            params["status"] = status
        if date:
            try:
                datetime.strptime(date, '%Y-%m-%d')  # Check date format
                params["date"] = date
            except ValueError:
                logging.error("Invalid date format. It must be in YYYY-MM-DD format.")
                return None  # Return None in case of error

        logging.info(f"Retrieving matches for league {league_id} and season {season}.")
        response = self.api_client.send_request(endpoint, params=params)

        if response and "error" in response:
            logging.error(f"Matches for league {league_id} could not be retrieved.")
            return None  # Return None in case of error

        logging.info(f"Matches for league {league_id} successfully retrieved.")
        return response