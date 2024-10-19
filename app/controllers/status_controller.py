from flask import Blueprint
from app.api.status_service import StatusService

# Define a Blueprint for the status routes
status_controller = Blueprint('status_controller', __name__)
status_service = StatusService()

# Route for /status
@status_controller.route('/status', methods=['GET'])
def get_status():
    """Controller to handle the status API endpoint."""
    response = status_service.get_status()
    
    if response:
        return response, 200  # Return the API response directly if successful
    else:
        return {"error": "Failed to retrieve status"}, 500  # Return an error message if the request fails