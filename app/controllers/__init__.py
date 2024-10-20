from .home_controller import home_controller  # Home controller
from .status_controller import status_controller  # Status controller
from .countries_controller import countries_controller  # Countries controller
from .seasons_controller import seasons_controller # Seasons controller
from .season_countries_controller import season_countries_controller # Season countries controller
from .leagues_controller import leagues_controller # Leagues controller

# List of all Blueprints
blueprints = [
    home_controller,
    status_controller,
    countries_controller,
    seasons_controller,
    season_countries_controller,
    leagues_controller,
]