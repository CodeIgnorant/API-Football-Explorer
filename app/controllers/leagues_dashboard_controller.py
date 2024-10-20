from flask import Blueprint, render_template
from app.api.leagues_service import Leagues  # Import the Leagues class

# Create a Blueprint for handling leagues by season and country
leagues_dashboard_controller = Blueprint('leagues_dashboard_controller', __name__)

# Initialize services
leagues_service = Leagues()  # Instantiate the Leagues service

# Route for retrieving leagues by season and country
@leagues_dashboard_controller.route('/seasons/<int:season>/<int:league_id>', methods=['GET'])
def get_leagues_dashboard(season, league_id):
    """Show the leagues dashboard for a specific season and league."""
    # Pass season and league_id as kwargs to the leagues service
    response = leagues_service.get_leagues(season=season, id=league_id)

    if response and "response" in response:
        league_info = response['response'][0]  # İlk öğeyi alın çünkü liste içinde tek lig var
        return render_template('leagues_dashboard.html', league_info=league_info, season=season)
    else:
        return {"error": "Failed to retrieve league information"}, 500