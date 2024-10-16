import os
import logging
import re

class Config:
    api_url = os.getenv('API_URL', "https://v3.football.api-sports.io")
    api_key = os.getenv('API_KEY')
    db_path = os.getenv('DATABASE_URL', 'sqlite:///database.db')  # SQLite database path

    @staticmethod
    def check_env_variables():
        if not Config.api_url:
            logging.error("Missing API URL environment variable. Please check the environment variables.")
            raise ValueError("Missing API URL environment variable.")
        
        if not re.match(r'^https?://', Config.api_url):
            logging.error("Invalid API URL format.")
            raise ValueError("Invalid API URL format.")

        logging.info("API URL successfully read.")

        if not Config.api_key:
            logging.error("Missing API Key environment variable. Please check the environment variables.")
            raise ValueError("Missing API Key environment variable.")
        logging.info("API Key successfully read.")

        if not Config.db_path:
            logging.error("Missing database path environment variable. Please check the environment variables.")
            raise ValueError("Missing database path environment variable.")
        logging.info("Database path successfully read.")