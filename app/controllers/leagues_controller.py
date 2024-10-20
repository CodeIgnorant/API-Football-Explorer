from flask import Blueprint, render_template
from app.api.leagues_service import Leagues  # Import the Leagues class

# Create a Blueprint for handling leagues by season and country
leagues_controller = Blueprint('leagues_controller', __name__)

# Initialize services
leagues_service = Leagues()  # Instantiate the Leagues service

# Route for retrieving leagues by season and country
@leagues_controller.route('/seasons/<int:season>/<string:country>', methods=['GET'])
def get_leagues_by_season_and_country(season, country):
    """Show the leagues for a specific season and country."""
    # Pass season and country as kwargs to the leagues service
    response = leagues_service.get_leagues(season=season, country=country)

    if response and "response" in response:
        # Sort leagues by league ID
        sorted_leagues = sorted(response['response'], key=lambda x: x['league']['id'])
        # Render leagues.html and pass the sorted leagues
        return render_template('leagues.html', leagues=sorted_leagues, season=season, country=country)
    else:
        return {"error": "Failed to retrieve leagues"}, 500