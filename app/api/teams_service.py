import logging
from app.api.api_client import APIClient

class Teams:
    def __init__(self):
        self.api_client = APIClient()

    def get_teams(self, **kwargs):
        """Method used to retrieve team information."""
        endpoint = "teams"

        logging.info("Retrieving team information.")
        
        # Send request with APIClient
        response = self.api_client.send_request(endpoint, **kwargs)

        if response and "error" in response:
            logging.error("Teams could not be retrieved.")
            return None  # Return None in case of error

        logging.info("Teams successfully retrieved.")
        return response