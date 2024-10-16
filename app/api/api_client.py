import requests
import logging
from app.api.api_connection import APIConnection

class APIClient:
    def __init__(self):
        # Create APIConnection
        self.api_connection = APIConnection()  # No need to get values from Config
        self.base_url = self.api_connection.api_url
        self.headers = self.api_connection.headers
        self.timezone = "Europe/Istanbul"  # We set the timezone as a constant

    def send_request(self, endpoint, params=None):
        """Method used to make a general API request.
        It is assumed that the response will always return a list.
        """
        url = f"{self.base_url}/{endpoint}"
        logging.info(f"URL created: {url}")

        params = params or {}
        try:
            response = requests.get(url, headers=self.headers, params=params, timeout=10)
            response.raise_for_status()  # Check for HTTP errors
            logging.info("API request successful!")

            return response.json()  # Return in JSON format
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as req_err:
            logging.error(f"An error occurred during the API request: {req_err}")

        return {"error": "API request failed."}  # Returns error message in case of failure