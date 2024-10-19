from flask import Blueprint, render_template

# Create a Blueprint for the home route
home_controller = Blueprint('home_controller', __name__)

# Define a route for the home page
@home_controller.route('/')
def home():
    """Home page route."""
    return render_template('index.html')  # Render index.html templates