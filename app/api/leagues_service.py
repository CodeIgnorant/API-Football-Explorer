import logging
from app.api.api_client import APIClient

class Leagues:
    def __init__(self):
        self.api_client = APIClient()

    def get_leagues(self, **kwargs):
        """Method used to retrieve league information based on the season."""
        endpoint = "leagues"

        logging.info("Retrieving league information.")
        
        response = self.api_client.send_request(endpoint, **kwargs)

        if response and "error" in response:
            logging.error("Leagues could not be retrieved.")
            return None  # Return None in case of error

        logging.info("Leagues successfully retrieved.")
        return response