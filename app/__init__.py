from flask import Flask
import logging

# Start the Flask application
app = Flask(__name__)

# Load the Config file
app.config.from_object('app.settings.config.Config')

# Add logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Import and register Blueprints
from app.controllers.status_controller import status_controller

# Register the Blueprint
app.register_blueprint(status_controller)

# Include other controllers if needed
from app.controllers import *  # Import all other controllers if necessary