import logging
from app.api.api_client import APIClient

class Leagues:
    def __init__(self):
        self.api_client = APIClient()

    def get_leagues(self, **kwargs):
        """Method to retrieve leagues using dynamic parameters with kwargs."""
        endpoint = "leagues"
        
        logging.info(f"Retrieving leagues with parameters: {kwargs}")
        
        # Send request to the API with kwargs as parameters
        response = self.api_client.send_request(endpoint, **kwargs)

        if response and "error" in response:
            logging.error("Leagues could not be retrieved.")
            return None  # Return None in case of error

        logging.info("Leagues successfully retrieved.")
        return response

    def get_leagues_by_season_and_country(self, season, country, **kwargs):
        """Method to retrieve leagues by season and country using kwargs."""
        endpoint = "leagues"
        
        # Add season and country to params, and update with additional kwargs
        params = {
            'season': season,
            'country': country
        }
        params.update(kwargs)  # Add additional kwargs to the params

        logging.info(f"Retrieving leagues for season {season} and country {country}.")
        
        response = self.api_client.send_request(endpoint, **params)

        if response and "error" in response:
            logging.error(f"Leagues could not be retrieved for season {season} and country {country}.")
            return None  # Return None in case of error

        logging.info(f"Leagues successfully retrieved for season {season} and country {country}.")
        return response