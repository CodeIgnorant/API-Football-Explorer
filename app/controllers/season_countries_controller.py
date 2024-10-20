from flask import Blueprint, render_template
from app.api.countries_service import Countries

# Create a Blueprint for handling countries by season
season_countries_controller = Blueprint('season_countries_controller', __name__)
countries_service = Countries()

# Route for retrieving countries by season
@season_countries_controller.route('/seasons/<int:season>/countries', methods=['GET'])
def get_countries_by_season(season):
    """Show the list of countries for a specific season, but the country list is the same for all seasons."""
    response = countries_service.get_countries()

    if response:
        # Pass the full response and season to the new template
        return render_template('season_countries.html', countries=response, season=season)
    else:
        return {"error": "Failed to retrieve countries"}, 500