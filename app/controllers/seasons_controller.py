from flask import Blueprint, render_template
from app.api.seasons_service import SeasonsService

# Create a Blueprint for seasons
seasons_controller = Blueprint('seasons_controller', __name__)
seasons_service = SeasonsService()

# Route for retrieving the list of all available seasons
@seasons_controller.route('/seasons', methods=['GET'])
def get_seasons():
    """Controller to handle the seasons API endpoint."""
    response = seasons_service.get_seasons()

    if response and "response" in response:
        # Render the HTML template and pass the seasons data
        return render_template('seasons.html', seasons=response['response'])
    else:
        return {"error": "Failed to retrieve seasons"}, 500  # Return error message if the request fails