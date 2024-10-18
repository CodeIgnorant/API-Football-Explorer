# API Endpoint Parameter Configuration
# 
# required_params: A list of parameters that must be provided in the request.
# optional_params: A list of parameters that can be optionally included in the request.

endpoint_config = {
    "status": {
        "required_params": [],
        "optional_params": []
    },
    "timezone": {
        "required_params": [],
        "optional_params": []
    },
    "countries": {
        "required_params": [],
        "optional_params": ["name", "code", "search", "season"]
    },
    "leagues": {
        "required_params": ["season"],
        "optional_params": ["id", "name", "country", "code", "team", "type", "current", "search", "last", "season"]
    },
    "leagues/seasons": {
        "required_params": [],
        "optional_params": []
    },
    "teams": {
        "required_params": [],
        "optional_params": ["id", "name", "league", "season", "country", "code", "venue", "search"]
    },
    "teams/statistics": {
        "required_params": ["league", "season", "team"],
        "optional_params": ["date"]
    },
    "teams/seasons": {
        "required_params": ["team"],
        "optional_params": []
    },
    "venues": {
        "required_params": [],
        "optional_params": ["id", "name", "city", "country", "search"]
    },
    "standings": {
        "required_params": ["season"],
        "optional_params": ["league", "team"]
    },
    "fixtures/rounds": {
        "required_params": ["league", "season"],
        "optional_params": ["current", "dates", "timezone"]
    },
    "fixtures": {
        "required_params": [],
        "optional_params": ["id", "ids", "live", "date", "league", "season", "team", "last", "next", "from", "to", "round", "status", "venue", "timezone"]
    },
    "fixtures/headtohead": {
        "required_params": ["h2h"],
        "optional_params": ["date", "league", "season", "last", "next", "from", "to", "status", "venue", "timezone"]
    },
    "fixtures/statistics": {
        "required_params": ["fixture"],
        "optional_params": ["team", "type", "half"]
    },
    "fixtures/events": {
        "required_params": ["fixture"],
        "optional_params": ["team", "player", "type"]
    },
    "fixtures/lineups": {
        "required_params": ["fixture"],
        "optional_params": ["team", "player", "type"]
    },
    "fixtures/players": {
        "required_params": ["fixture"],
        "optional_params": ["team"]
    },
    "injuries": {
        "required_params": [],
        "optional_params": ["league", "season", "fixture", "team", "player", "date", "ids", "timezone"]
    },
    "predictions": {
        "required_params": ["fixture"],
        "optional_params": []
    }
}