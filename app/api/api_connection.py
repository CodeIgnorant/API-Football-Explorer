import requests
import logging
from app.settings.config import Config  # Import Config

class APIConnection:
    def __init__(self):
        """
        The APIConnection class is used to establish a connection with the API.
        The API URL and API key are retrieved from Config.
        """
        self.api_url = Config.api_url  # Get API URL from Config
        self.api_key = Config.api_key  # Get API key from Config

        # API Key check and output
        if not self.api_key:
            logging.error("API Key not found. Please provide a valid API key.")
            raise ValueError("API Key not found.")
        else:
            logging.info(f"API Key successfully retrieved: {self.api_key[:4]}****")

        # Headers - The API only accepts certain headers
        self.headers = {
            "x-apisports-key": self.api_key  # Apisports API key
        }

    def test_connection(self):
        """Method that tests the API connection."""
        try:
            response = requests.get(self.api_url, headers=self.headers, timeout=10)
            response.raise_for_status()  # Raises exception on error
            logging.info("API connection successful!")  # Successful connection log
            return True  # Connection successful
        except requests.exceptions.RequestException as req_err:
            logging.error(f"API connection failed! Error: {req_err}")
            return False  # Connection failed