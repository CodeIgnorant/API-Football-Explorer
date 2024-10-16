import logging
from app.api.api_client import APIClient

class Timezone:
    def __init__(self, api_client: APIClient):
        self.api_client = api_client

    def get_timezones(self):
        """Method used to retrieve all available timezones."""
        endpoint = "timezone"
        logging.info("Retrieving all available timezones.")
        return self.api_client.send_request(endpoint)