from app.api.api_client import APIClient
import logging

class Leagues:
    def __init__(self, api_client: APIClient):
        self.api_client = api_client

    def get_leagues_country_current_type(self, country_name, league_type):
        """Method to retrieve active leagues of a specific type in a given country."""
        if not country_name or len(country_name) < 2:
            logging.error("Invalid country name. It must be at least 2 characters long.")
            return None

        if league_type not in ["league", "cup"]:
            logging.error("Invalid league type. It must be 'league' or 'cup'.")
            return None

        endpoint = "leagues"
        params = {
            "country": country_name,
            "type": league_type,
            "current": "true"
        }
        logging.info(f"Retrieving active {league_type} leagues in {country_name}.")
        
        # Send request with APIClient
        response = self.api_client.send_request(endpoint, **params)

        if response is None or 'response' not in response or len(response['response']) == 0:
            logging.error("Leagues could not be retrieved or unexpected structure in API response: %s", response)
            return None

        logging.info("Leagues successfully retrieved.")
        return response['response']

    def get_leagues_country_season_type(self, country_name, season, league_type):
        """Method to retrieve leagues of a specific type and season in a given country."""
        if not country_name or len(country_name) < 2:
            logging.error("Invalid country name. It must be at least 2 characters long.")
            return None

        if league_type not in ["league", "cup"]:
            logging.error("Invalid league type. It must be 'league' or 'cup'.")
            return None

        endpoint = "leagues"
        params = {
            "country": country_name,
            "season": season,
            "type": league_type
        }
        logging.info(f"Retrieving {league_type} leagues in {country_name} for the season.")
        
        # Send request with APIClient
        response = self.api_client.send_request(endpoint, **params)

        if response is None or 'response' not in response or len(response['response']) == 0:
            logging.error("Leagues could not be retrieved or unexpected structure in API response: %s", response)
            return None

        logging.info("Leagues successfully retrieved.")
        return response['response']