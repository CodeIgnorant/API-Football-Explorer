import requests
import logging
from app.api.api_connection import APIConnection


class APIClient:
    def __init__(self):
        # Create APIConnection
        self.api_connection = APIConnection()
        self.base_url = self.api_connection.api_url
        self.headers = self.api_connection.headers
        self.timezone = "Europe/Istanbul"  # We set the timezone as a constant

    def send_request(self, endpoint, **kwargs):
        """
        Method used to make a general API request.
        :param endpoint: API endpoint to hit.
        :param kwargs: Dictionary of optional parameters to send in the request.
        """
        # Base URL and endpoint combination
        url = f"{self.base_url}/{endpoint}"

        # Log the base URL before adding query parameters
        logging.info(f"Base URL created: {url}")

        try:
            # Send GET request with query parameters (kwargs)
            response = requests.get(
                url, headers=self.headers, params=kwargs, timeout=10)
            response.raise_for_status()  # Check for HTTP errors

            # Log the final full URL (with query parameters)
            logging.info(f"Full URL with params: {response.url}")
            logging.info("API request successful!")

            return response.json()  # Return the response in JSON format
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as req_err:
            logging.error(
                f"An error occurred during the API request: {req_err}")

        return {"error": "API request failed."}
