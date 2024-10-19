from flask import render_template  # Import the render_template function
from app import app  # Import the app instance
from app.api.countries_service import Countries  # Import the Countries class
from app.api.api_client import APIClient  # Import the APIClient class
import logging  # Required for logging

@app.route('/countries')
def get_countries():
    """Function that makes a request to the API to retrieve all countries."""
    api_client = APIClient()  # Create an APIClient instance
    countries_service = Countries(api_client)  # Pass the APIClient instance
    countries = countries_service.get_countries()  # Retrieve all countries
    
    # Check the response
    if countries is not None:
        logging.info("Countries successfully retrieved.")  # Success message only
        return render_template('countries.html', countries=countries)  # Render the HTML template
    else:
        logging.error("Countries could not be retrieved!")  # Error logging
        return render_template('error.html', message="Countries could not be retrieved!")  # Render the error page