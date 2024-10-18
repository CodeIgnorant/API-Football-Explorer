import requests
import logging
from app.api.api_connection import APIConnection
from app.settings.endpoint_config import endpoint_config  # Import the endpoint configuration

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
        # Get the endpoint configuration
        endpoint_params = endpoint_config.get(endpoint, {})
        required_params = endpoint_params.get("required_params", [])
        optional_params = endpoint_params.get("optional_params", [])

        # Validate required parameters
        missing_params = [param for param in required_params if param not in kwargs]
        if missing_params:
            logging.error(f"Missing required parameters: {missing_params}")
            return {"error": f"Missing required parameters: {missing_params}"}

        # Filter only allowed parameters (both required and optional)
        allowed_params = {key: value for key, value in kwargs.items() if key in required_params + optional_params}

        # Log filtered parameters
        logging.info(f"Filtered parameters for {endpoint}: {allowed_params}")

        # Base URL and endpoint combination
        url = f"{self.base_url}/{endpoint}"

        try:
            # Send GET request with query parameters (allowed_params)
            response = requests.get(
                url, headers=self.headers, params=allowed_params, timeout=10)
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