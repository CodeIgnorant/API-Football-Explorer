from flask import Blueprint
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
        return response, 200  # Directly return the response if successful
    else:
        return {"error": "Failed to retrieve countries"}, 500  # Return error message if the request fails