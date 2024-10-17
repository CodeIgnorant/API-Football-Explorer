import os
import logging

class Config:
    # Load the API URL from environment variables or use a default value
    api_url = os.getenv('API_URL', "https://v3.football.api-sports.io")
    
    # Load the API key from environment variables; provide a default key for development
    api_key = os.getenv('API_KEY', 'your_test_api_key')
    
    # Load the database path from environment variables or use a default SQLite database
    db_path = os.getenv('DATABASE_URL', 'sqlite:///database.db')

    @staticmethod
    def check_env_variables():
        # Check if the API URL is set
        if not Config.api_url:
            logging.error("Missing API URL environment variable. Please check the environment variables.")
            raise ValueError("Missing API URL environment variable.")
        logging.info("API URL successfully read.")

        # Check if the API key is set
        if not Config.api_key:
            logging.error("Missing API Key environment variable. Please check the environment variables.")
            raise ValueError("Missing API Key environment variable.")
        logging.info("API Key successfully read.")

        # Check if the database path is set
        if not Config.db_path:
            logging.error("Missing database path environment variable. Please check the environment variables.")
            raise ValueError("Missing database path environment variable.")
        logging.info("Database path successfully read.")
