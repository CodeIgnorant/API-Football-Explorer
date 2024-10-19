from app.api.api_client import APIClient
import logging

class StatusService:
    def __init__(self):
        self.api_client = APIClient()

    def get_status(self, **kwargs):
        """Method to request the status from the API, with optional parameters."""
        response = self.api_client.send_request('status', **kwargs)
        
        if response and 'error' not in response:
            logging.info("Status retrieved successfully")
            logging.debug(f"Response data: {response}")  # Log detailed response data
            return response
        else:
            logging.error("Failed to retrieve status")
            return None