from flask import Flask
import logging

# Start the Flask application
app = Flask(__name__)

# Load the Config file
app.config.from_object('app.settings.config.Config')

# Add logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Import the blueprints list from controllers/__init__.py
from app.controllers import blueprints

# Register all Blueprints from the list
for blueprint in blueprints:
    app.register_blueprint(blueprint)