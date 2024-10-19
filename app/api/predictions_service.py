import logging
from app.api.api_client import APIClient

class Predictions:
    def __init__(self):
        self.api_client = APIClient()

    def get_predictions(self, fixture, **kwargs):
        """Method used to retrieve predictions for a specific fixture."""
        endpoint = "predictions"
        
        # Prepare parameters dictionary
        params = {
            "fixture": fixture,
        }

        logging.info(f"Retrieving predictions for fixture {fixture}.")
        
        # Send request with APIClient
        response = self.api_client.send_request(endpoint, **params)

        if response and "error" in response:
            logging.error(f"Predictions for fixture {fixture} could not be retrieved.")
            return None  # Return None in case of error

        logging.info(f"Predictions for fixture {fixture} successfully retrieved.")
        return response