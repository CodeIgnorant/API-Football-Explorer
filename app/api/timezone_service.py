import logging
from app.api.api_client import APIClient

class Timezone:
    def __init__(self, api_client: APIClient):
        self.api_client = api_client

    def get_timezones(self, **kwargs):
        """Method used to retrieve all available timezones."""
        endpoint = "timezone"
        logging.info("Retrieving all available timezones.")

        response = self.api_client.send_request(endpoint, **kwargs)
        
        if response and 'error' not in response:
            logging.info("Timezones retrieved successfully")
            logging.debug(f"Response data: {response}")  # Log detailed response data
            return response
        else:
            logging.error("Failed to retrieve timezones")
            return None