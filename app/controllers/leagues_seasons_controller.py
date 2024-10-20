from app.api.leagues_seasons_service import LeaguesSeasons

# Define a service instance for leagues seasons
leagues_seasons_service = LeaguesSeasons()

def get_leagues_seasons():
    """Function to return the leagues seasons data."""
    response = leagues_seasons_service.get_leagues_seasons()

    if response and "response" in response:
        # Return the JSON response directly
        return response['response']
    else:
        return {"error": "Failed to retrieve leagues seasons"}