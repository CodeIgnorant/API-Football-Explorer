import logging
from app.api.api_client import APIClient

class FixturesPlayers:
    def __init__(self):
        self.api_client = APIClient()

    def get_fixtures_players(self, fixture, **kwargs):
        """Method used to retrieve players for a specific fixture."""
        endpoint = "fixtures/players"
        
        # Prepare parameters dictionary
        params = {
            "fixture": fixture,
        }
        # Include optional parameters
        params.update(kwargs)

        logging.info(f"Retrieving players for fixture {fixture}.")
        
        # Send request with APIClient
        response = self.api_client.send_request(endpoint, **params)

        if response and "error" in response:
            logging.error(f"Players for fixture {fixture} could not be retrieved.")
            return None  # Return None in case of error

        logging.info(f"Players for fixture {fixture} successfully retrieved.")
        return response