from flask import Blueprint, render_template
from app.api.countries_service import Countries

# Create a Blueprint for countries
countries_controller = Blueprint('countries_controller', __name__)
countries_service = Countries()

# Route for retrieving the list of all available countries
@countries_controller.route('/countries', methods=['GET'])
def get_countries():
    """Controller to handle the countries API endpoint."""
    response = countries_service.get_countries()

    if response:
        return render_template('countries.html', countries=response['response'])  # Render HTML template
    else:
        return {"error": "Failed to retrieve countries"}, 500  # Return error message if the request fails