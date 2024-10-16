import logging
from app import db
from app.models import *  # Import all models

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_database():
    try:
        db.create_all()  # Create tables for all defined models
        logging.info("Database and tables successfully created.")
    except Exception as e:
        logging.error(f"An error occurred while creating the database: {e}")

if __name__ == "__main__":
    create_database()  # Create the database when the script is run