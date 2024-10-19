import logging
from app.api.api_client import APIClient

class FixturesEvents:
    def __init__(self):
        self.api_client = APIClient()

    def get_fixtures_events(self, fixture, **kwargs):
        """Method used to retrieve events for a specific fixture."""
        endpoint = "fixtures/events"
        
        # Prepare parameters dictionary
        params = {
            "fixture": fixture,
        }
        # Include optional parameters
        params.update(kwargs)

        logging.info(f"Retrieving events for fixture {fixture}.")
        
        # Send request with APIClient
        response = self.api_client.send_request(endpoint, **params)

        if response and "error" in response:
            logging.error(f"Events for fixture {fixture} could not be retrieved.")
            return None  # Return None in case of error

        logging.info(f"Events for fixture {fixture} successfully retrieved.")
        return response