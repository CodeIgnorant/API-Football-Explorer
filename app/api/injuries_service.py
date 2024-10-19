import logging
from app.api.api_client import APIClient

class Injuries:
    def __init__(self, api_client: APIClient):
        self.api_client = api_client

    def get_injuries(self, **kwargs):
        """Method used to retrieve injury information."""
        endpoint = "injuries"
        
        logging.info("Retrieving injury information.")
        
        # Send request with APIClient; no required params to validate
        response = self.api_client.send_request(endpoint, **kwargs)

        if response and "error" in response:
            logging.error("Injuries could not be retrieved.")
            return None  # Return None in case of error

        logging.info("Injuries successfully retrieved.")
        return response