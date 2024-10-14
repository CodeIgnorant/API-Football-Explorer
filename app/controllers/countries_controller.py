from flask import render_template  # render_template fonksiyonunu içe aktar
from app import app  # app nesnesini içe aktar
from app.api.country_service import Countries  # Countries sınıfını içe aktar
from app.api.api_client import APIClient  # APIClient sınıfını içe aktar
from app.settings.config import Config  # Config sınıfını içe aktar
import logging  # Loglama için gerekli

@app.route('/countries')
def get_all_countries():
    """Tüm ülkeleri almak için API'den istek yapan fonksiyon."""
    config = Config()  # Config'ten API bilgilerini al
    api_client = APIClient(api_url=config.api_url, api_key=config.api_key)  # Gerekli argümanları geç
    countries_service = Countries(api_client)  # APIClient nesnesini geçiriyoruz
    countries = countries_service.get_all_countries()  # Tüm ülkeleri al
    
    # Yanıtın kontrolü
    if countries is not None:
        logging.info(f"Ülkeler başarıyla alındı: {countries}")  # Loglama
        return render_template('countries.html', countries=countries)  # HTML şablonunu renderla
    else:
        logging.error("Ülkeler alınamadı!")  # Hata loglama
        return render_template('error.html', message="Ülkeler alınamadı!")  # Hata sayfasını renderla
