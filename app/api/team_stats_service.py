import logging
from app.api.api_client import APIClient

class TeamStats:
    def __init__(self, api_client: APIClient):
        self.api_client = api_client

    def get_team_statistics(self, team_id, league_id, season, date=None):
        """Method used to retrieve the statistics of a specific team for a given league and season."""
        endpoint = "teams/statistics"
        params = {
            "team": team_id,
            "league": league_id,
            "season": season
        }
        if date:
            params["date"] = date
        logging.info(f"Retrieving statistics for team {team_id}, league {league_id}, season {season}.")
        response = self.api_client.send_request(endpoint, params=params)

        if response and "error" in response:
            logging.error(f"Statistics for team {team_id} could not be retrieved.")
            return None  # Return None in case of error

        logging.info(f"Statistics for team {team_id} successfully retrieved.")
        return response