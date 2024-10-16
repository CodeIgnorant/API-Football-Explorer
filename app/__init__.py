from flask import Flask
import logging

# Start the Flask application
app = Flask(__name__)

# Load the Config file
app.config.from_object('app.settings.config.Config')

# Add logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Include the controllers
from app.controllers import *  # Import all controllers at once