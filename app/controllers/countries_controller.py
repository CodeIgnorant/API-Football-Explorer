import time
from flask import Blueprint, render_template
from app.api.countries_service import Countries

# Create a Blueprint for countries
countries_controller = Blueprint('countries_controller', __name__)
countries_service = Countries()

# Route for retrieving the list of all available countries
@countries_controller.route('/countries', methods=['GET'])
def get_countries():
    """Controller to handle the countries API endpoint."""
    
    start_time = time.time()  # Start time for page generation
    
    response = countries_service.get_countries()

    if response:
        total_time = time.time() - start_time  # Calculate total time taken to generate the page
        return render_template('countries.html', countries=response, total_time=total_time)
    else:
        return {"error": "Failed to retrieve countries"}, 500  # Return error message if the request fails