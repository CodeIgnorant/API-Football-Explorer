import logging
from app.api.api_client import APIClient

class Standings:
    def __init__(self):
        self.api_client = APIClient()

    def get_standings(self, season, **kwargs):
        """Method used to retrieve standings based on a specific season."""
        endpoint = "standings"
        
        # Prepare parameters dictionary
        params = {
            "season": season,
        }
        # Include optional parameters
        params.update(kwargs)

        logging.info(f"Retrieving standings for season {season}.")
        
        # Send request with APIClient
        response = self.api_client.send_request(endpoint, **params)

        if response and "error" in response:
            logging.error(f"Standings for season {season} could not be retrieved.")
            return None  # Return None in case of error

        logging.info(f"Standings for season {season} successfully retrieved.")
        return response