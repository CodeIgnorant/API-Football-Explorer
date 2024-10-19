import logging
from app.api.api_client import APIClient

class TeamsSeasons:
    def __init__(self, api_client: APIClient):
        self.api_client = api_client

    def get_teams_seasons(self, team_id, **kwargs):
        """Method used to retrieve available seasons for a specific team."""
        endpoint = "teams/seasons"
        
        # Prepare parameters dictionary
        params = {
            "team": team_id,
        }
        
        logging.info(f"Retrieving seasons for team {team_id}.")
        
        # Send request with APIClient
        response = self.api_client.send_request(endpoint, **params)

        if response and "error" in response:
            logging.error(f"Seasons for team {team_id} could not be retrieved.")
            return None  # Return None in case of error

        logging.info(f"Seasons for team {team_id} successfully retrieved.")
        return response