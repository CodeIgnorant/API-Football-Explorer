from flask import Response
from app import app
from app.api.connection_tester import ConnectionTester  # Bağlantı tester'ı import ediyoruz
from app.settings.config import Config
import logging
import json

# Loglama ayarları
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/test-api')
def test_api():
    """API bağlantısını test eden fonksiyon."""
    config = Config()
    
    # ConnectionTester'ı başlat
    tester = ConnectionTester(api_url=config.api_url, api_key=config.api_key)

    logging.info("API bağlantısı test ediliyor...")  # Test sürecinin başlangıcını logla
    
    if tester.test_connection():
        logging.info("API bağlantısı başarılı!")
        response = {"message": "API bağlantısı başarılı!", "status": "success"}
    else:
        logging.error("API bağlantısı başarısız!")
        response = {"message": "API bağlantısı başarısız!", "status": "fail"}

    return Response(json.dumps(response, ensure_ascii=False), content_type="application/json; charset=utf-8")
