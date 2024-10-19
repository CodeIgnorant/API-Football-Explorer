import logging
from app.api.api_client import APIClient

class Countries:
    def __init__(self, api_client: APIClient):  # Takes APIClient as a parameter
        self.api_client = api_client  # Receives the APIClient instance

    def get_countries(self, **kwargs):
        """Method used to retrieve the list of all available countries."""
        endpoint = "countries"
        response = self.api_client.send_request(endpoint, **kwargs)  # Send request with APIClient
        logging.debug(f"Response from API: {response}")  # Lower level log

        if response is None or len(response) == 0:
            logging.error("Error received from API or response is empty.")
            return None  # Return None in case of error

        logging.info("All countries successfully retrieved.")
        return response  # Return API response

    def get_country_by_name(self, name):
        """Method used to retrieve country information by country name."""
        if len(name) < 3:
            logging.error("Country name must be at least 3 characters long.")
            return None  # Return None in case of error

        endpoint = "countries"
        params = {"name": name}  # Create a params dictionary for the request
        response = self.api_client.send_request(endpoint, **params)  # Send request with APIClient

        if response is None or len(response) == 0:
            logging.error(f"Information for country {name} could not be retrieved.")
            return None  # Return None in case of error

        logging.info(f"Information for country {name} successfully retrieved.")
        return response  # Return API response

    def get_country_by_code(self, code):
        """Method used to retrieve country information by country code."""
        if len(code) < 2 or len(code) > 6:
            logging.error("Country code must be between 2 and 6 characters long.")
            return None  # Return None in case of error

        endpoint = "countries"
        params = {"code": code}  # Create a params dictionary for the request
        response = self.api_client.send_request(endpoint, **params)  # Send request with APIClient

        if response is None or len(response) == 0:
            logging.error(f"Information for country {code} could not be retrieved.")
            return None  # Return None in case of error

        logging.info(f"Information for country {code} successfully retrieved.")
        return response  # Return API response