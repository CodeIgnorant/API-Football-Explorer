from flask import jsonify  # jsonify fonksiyonunu içe aktar
from app import app  # app nesnesini içe aktar
from app.api.country_service import Countries  # Countries sınıfını içe aktar
from app.api.api_client import APIClient  # APIClient sınıfını içe aktar
import logging  # Loglama için gerekli

@app.route('/countries')
def get_all_countries():
    """Tüm ülkeleri almak için API'den istek yapan fonksiyon."""
    api_client = APIClient()  # APIClient örneği oluştur
    countries_service = Countries(api_client)  # Countries sınıfını başlat
    countries = countries_service.get_all_countries()  # Tüm ülkeleri al
    
    # Yanıtın kontrolü
    if countries is not None:
        logging.info(f"Ülkeler başarıyla alındı: {countries}")  # Loglama
        return jsonify(countries), 200  # Başarılı yanıt
    else:
        logging.error("Ülkeler alınamadı!")  # Hata loglama
        return jsonify({"message": "Ülkeler alınamadı!"}), 500  # Hata durumu
