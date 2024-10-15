from flask import Response
from app import app
from app.api.api_connection import APIConnection  # APIConnection sınıfını import ediyoruz
import logging
import json

# Loglama ayarları
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/test-api')
def test_api():
    """API bağlantısını test eden fonksiyon."""
    
    # APIConnection'ı başlat
    connection = APIConnection()

    logging.info("API bağlantısı test ediliyor...")  # Test sürecinin başlangıcını logla
    
    if connection.test_connection():
        logging.info("API bağlantısı başarılı!")
        response = {"message": "API bağlantısı başarılı!", "status": "success"}
    else:
        logging.error("API bağlantısı başarısız!")
        response = {"message": "API bağlantısı başarısız!", "status": "fail"}

    return Response(json.dumps(response, ensure_ascii=False), content_type="application/json; charset=utf-8")
