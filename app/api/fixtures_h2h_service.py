import logging
from app.api.api_client import APIClient

class FixturesHeadToHead:
    def __init__(self):
        self.api_client = APIClient()

    def get_fixtures_headtohead(self, h2h, **kwargs):
        """Method used to retrieve head-to-head fixtures information."""
        endpoint = "fixtures/headtohead"
        
        # Prepare parameters dictionary
        params = {
            "h2h": h2h,
        }
        # Include optional parameters
        params.update(kwargs)

        logging.info(f"Retrieving head-to-head fixtures for {h2h}.")
        
        # Send request with APIClient
        response = self.api_client.send_request(endpoint, **params)

        if response and "error" in response:
            logging.error(f"Head-to-head fixtures for {h2h} could not be retrieved.")
            return None  # Return None in case of error

        logging.info(f"Head-to-head fixtures for {h2h} successfully retrieved.")
        return response