from flask import jsonify  # jsonify fonksiyonunu içe aktar
from app import app  # app nesnesini içe aktar
from app.api.api_connection import APIConnection  # APIConnection sınıfını içe aktar
import logging  # Loglama için gerekli

@app.route('/test-api')
def test_api():
    """API bağlantısını test eden fonksiyon."""
    api_connection = APIConnection()  # APIConnection kullanımı
    if api_connection.test_connection():
        logging.info("API bağlantısı başarılı!")  # Başarılı bağlantı logu
        return "API bağlantısı başarılı!"  # Başarılı yanıt
    else:
        logging.error("API bağlantısı başarısız!")  # Başarısız bağlantı logu
        return "API bağlantısı başarısız!"  # Başarısız yanıt
