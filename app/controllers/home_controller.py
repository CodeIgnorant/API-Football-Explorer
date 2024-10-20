from flask import Blueprint, render_template
from app.api.leagues_seasons_service import LeaguesSeasons

# Define a Blueprint for the home routes
home_controller = Blueprint('home_controller', __name__)
leagues_seasons_service = LeaguesSeasons()

# Route for the home page (index)
@home_controller.route('/', methods=['GET'])
def index():
    """Home page showing available seasons."""
    seasons = leagues_seasons_service.get_leagues_seasons()

    if seasons and "response" in seasons:
        # Sort seasons in descending order (biggest to smallest)
        sorted_seasons = sorted(seasons['response'], reverse=True)
        return render_template('index.html', seasons=sorted_seasons)
    else:
        return {"error": "Failed to retrieve seasons"}, 500