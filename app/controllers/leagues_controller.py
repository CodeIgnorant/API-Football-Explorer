from flask import render_template
from app import app
from app.api.league_service import Leagues  # Leagues sınıfını içe aktar
from app.api.api_client import APIClient  # APIClient sınıfını içe aktar
import logging

@app.route('/<country_name>/leagues')  # Ülke adı ile aktif ligler
def get_country_leagues(country_name):
    """Belirli bir ülkenin aktif liglerini almak için route."""
    api_client = APIClient()  # APIClient örneği oluştur
    leagues_service = Leagues(api_client)  # Leagues sınıfını başlat

    # Ülkeye ait aktif ligleri al
    leagues = leagues_service.get_leagues_country_current_type(country_name, "league")

    # Loglama ile dönen veriyi kontrol et
    logging.info(f"{country_name} ülkesindeki aktif ligler: {leagues}")

    # Eğer ligler varsa, şablonu renderla
    if leagues:
        return render_template('country_leagues.html', country_name=country_name, leagues=leagues)
    else:
        logging.error(f"{country_name} ülkesindeki ligler alınamadı.")
        return render_template('error.html', message="Ligler bulunamadı!"), 404  # Hata sayfasını renderla
