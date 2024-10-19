import logging
from app.api.api_client import APIClient

class FixturesStatistics:
    def __init__(self, api_client: APIClient):
        self.api_client = api_client

    def get_fixtures_statistics(self, fixture, **kwargs):
        """Method used to retrieve statistics for a specific fixture."""
        endpoint = "fixtures/statistics"
        
        # Prepare parameters dictionary
        params = {
            "fixture": fixture,
        }
        # Include optional parameters
        params.update(kwargs)

        logging.info(f"Retrieving statistics for fixture {fixture}.")
        
        # Send request with APIClient
        response = self.api_client.send_request(endpoint, **params)

        if response and "error" in response:
            logging.error(f"Statistics for fixture {fixture} could not be retrieved.")
            return None  # Return None in case of error

        logging.info(f"Statistics for fixture {fixture} successfully retrieved.")
        return response