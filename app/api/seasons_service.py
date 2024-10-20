import logging
from app.api.api_client import APIClient

class SeasonsService:
    def __init__(self):
        self.api_client = APIClient()

    def get_seasons(self, **kwargs):
        """Method used to retrieve available seasons."""
        endpoint = "leagues/seasons"

        logging.info("Retrieving available seasons.")
        
        # Send request to API
        response = self.api_client.send_request(endpoint, **kwargs)

        if not response or "error" in response:
            logging.error("Seasons could not be retrieved.")
            return None  # Return None in case of error

        logging.info("Seasons successfully retrieved.")
        return response  # Return the API response