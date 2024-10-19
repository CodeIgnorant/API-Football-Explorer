import logging
from app.api.api_client import APIClient

class Fixtures:
    def __init__(self):
        self.api_client = APIClient()

    def get_fixtures(self, **kwargs):
        """Method used to retrieve fixtures information."""
        endpoint = "fixtures"
        
        logging.info("Retrieving fixtures information.")
        
        # Send request with APIClient; no required params to validate
        response = self.api_client.send_request(endpoint, **kwargs)

        if response and "error" in response:
            logging.error("Fixtures could not be retrieved.")
            return None  # Return None in case of error

        logging.info("Fixtures successfully retrieved.")
        return response