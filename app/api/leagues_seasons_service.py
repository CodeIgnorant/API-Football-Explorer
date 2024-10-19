import logging
from app.api.api_client import APIClient

class LeaguesSeasons:
    def __init__(self):
        self.api_client = APIClient()

    def get_leagues_seasons(self, **kwargs):
        """Method used to retrieve available seasons for leagues."""
        endpoint = "leagues/seasons"

        logging.info("Retrieving available seasons for leagues.")
        
        response = self.api_client.send_request(endpoint, **kwargs)

        if response and "error" in response:
            logging.error("Seasons could not be retrieved.")
            return None  # Return None in case of error

        logging.info("Seasons successfully retrieved.")
        return response