import logging
from app.api.api_client import APIClient

class FixturesRounds:
    def __init__(self):
        self.api_client = APIClient()

    def get_fixtures_rounds(self, league, season, **kwargs):
        """Method used to retrieve fixtures rounds based on the league and season."""
        endpoint = "fixtures/rounds"
        
        # Prepare parameters dictionary
        params = {
            "league": league,
            "season": season,
        }
        # Include optional parameters
        params.update(kwargs)

        logging.info(f"Retrieving fixtures rounds for league {league} and season {season}.")
        
        # Send request with APIClient
        response = self.api_client.send_request(endpoint, **params)

        if response and "error" in response:
            logging.error(f"Fixtures rounds for league {league} and season {season} could not be retrieved.")
            return None  # Return None in case of error

        logging.info(f"Fixtures rounds for league {league} and season {season} successfully retrieved.")
        return response