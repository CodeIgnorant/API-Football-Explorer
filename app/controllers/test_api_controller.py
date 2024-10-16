from flask import Response
from app import app
from app.api.api_connection import APIConnection
import logging
import json

# Log settings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/test-api')
def test_api():
    """Function that tests the API connection."""
    
    # Start the APIConnection
    connection = APIConnection()

    logging.info("Testing the API connection...")
    
    if connection.test_connection():
        logging.info("API connection successful!")
        response = {"message": "API connection successful!", "status": "success"}
    else:
        logging.error("API connection failed!")
        response = {"message": "API connection failed!", "status": "fail"}

    return Response(json.dumps(response, ensure_ascii=False), content_type="application/json; charset=utf-8")