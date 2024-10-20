import time
from flask import Blueprint, render_template
from app.api.seasons_service import SeasonsService

# Create a Blueprint for seasons
seasons_controller = Blueprint('seasons_controller', __name__)
seasons_service = SeasonsService()

# Route for retrieving the list of all available seasons
@seasons_controller.route('/seasons', methods=['GET'])
def get_seasons():
    """Controller to handle the seasons API endpoint."""
    
    start_time = time.time()  # Start time for page generation
    
    response = seasons_service.get_seasons()

    if response:
        total_time = time.time() - start_time  # Calculate the total time taken
        # Pass the entire response to the template along with the total time
        return render_template('seasons.html', response=response, total_time=total_time)
    else:
        return {"error": "Failed to retrieve seasons"}, 500  # Return error message if the request fails