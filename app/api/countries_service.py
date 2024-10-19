import logging
from app.api.api_client import APIClient

class Countries:
    def __init__(self, api_client: APIClient):
        self.api_client = api_client

    def get_countries(self, **kwargs):
        """Method used to retrieve the list of all available countries."""
        endpoint = "countries"
        response = self.api_client.send_request(endpoint, **kwargs)
        logging.debug(f"Response from API: {response}")

        if not response:  # Checks for None or empty response
            logging.error("Error received from API or response is empty.")
            return None  # Return None in case of error

        logging.info("All countries successfully retrieved.")
        return response  # Return API response