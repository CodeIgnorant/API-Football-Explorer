import logging
from app.api.api_client import APIClient

class Venues:
    def __init__(self):
        self.api_client = APIClient()

    def get_venues(self, **kwargs):
        """Method used to retrieve venue information."""
        endpoint = "venues"
        
        logging.info("Retrieving venue information.")
        
        # Send request with APIClient; no required params to validate
        response = self.api_client.send_request(endpoint, **kwargs)

        if response and "error" in response:
            logging.error("Venues could not be retrieved.")
            return None  # Return None in case of error

        logging.info("Venues successfully retrieved.")
        return response