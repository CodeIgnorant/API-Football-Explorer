from app.api.api_client import APIClient
import logging

class StatusService:
    def __init__(self):
        self.api_client = APIClient()

    def get_status(self):
        """Method to request the status from the API."""
        response = self.api_client.send_request('status')
        if response and 'error' not in response:
            logging.info("Status retrieved successfully")
            return response
        else:
            logging.error("Failed to retrieve status")
            return None