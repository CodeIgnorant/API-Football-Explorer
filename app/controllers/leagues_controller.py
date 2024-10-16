from flask import render_template
from app import app
from app.api.league_service import Leagues  # Import the Leagues class
from app.api.api_client import APIClient  # Import the APIClient class
import logging

@app.route('/<country_name>/leagues')  # Active leagues by country name
def get_country_leagues(country_name):
    """Route to retrieve active leagues for a specific country."""
    api_client = APIClient()  # Create an APIClient instance
    leagues_service = Leagues(api_client)  # Initialize the Leagues class

    # Retrieve active leagues for the country
    leagues = leagues_service.get_leagues_country_current_type(country_name, "league")

    # Log the retrieved data
    logging.info(f"List of active leagues in {country_name}")

    # If there are leagues, render the template
    if leagues:
        return render_template('country_leagues.html', country_name=country_name, leagues=leagues)
    else:
        logging.error(f"Leagues could not be retrieved for {country_name}.")
        return render_template('error.html', message="Leagues not found!"), 404  # Render the error page