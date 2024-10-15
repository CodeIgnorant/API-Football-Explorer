import logging
from datetime import datetime
from app.api.api_client import APIClient

class Fixtures:
    def __init__(self, api_client: APIClient):
        self.api_client = api_client

    def get_fixture_id(self, fixture_id):
        """Belirli bir maç ID'sine göre maç bilgilerini almak için kullanılan metod."""
        if not isinstance(fixture_id, int) or fixture_id <= 0:
            logging.error("Geçersiz maç ID'si. Pozitif bir tam sayı olmalıdır.")
            return None  # Hata durumunda None döndür

        endpoint = "fixtures"
        params = {"id": fixture_id}
        logging.info(f"Fixture ID'si ile maç bilgileri alınıyor: {fixture_id}")
        response = self.api_client.send_request(endpoint, params=params)

        if response and "error" in response:
            logging.error("Maç bilgileri alınamadı.")
            return None  # Hata durumunda None döndür

        logging.info(f"{fixture_id} ID'li maç bilgileri başarıyla alındı.")
        return response

    def get_fixtures_league_season(self, league_id, season, status=None, date=None):
        """Belirli bir lig, sezon ve opsiyonel olarak duruma göre maçları almak için kullanılan metod."""
        if not isinstance(league_id, int) or league_id <= 0:
            logging.error("Geçersiz lig ID'si. Pozitif bir tam sayı olmalıdır.")
            return None  # Hata durumunda None döndür

        if not isinstance(season, int) or not (1000 <= season <= 9999):
            logging.error("Geçersiz sezon. Yıl formatında (YYYY) olmalıdır.")
            return None  # Hata durumunda None döndür

        endpoint = "fixtures"
        params = {
            "league": league_id,
            "season": season
        }
        if status:
            params["status"] = status
        if date:
            try:
                datetime.strptime(date, '%Y-%m-%d')  # Tarih formatını kontrol et
                params["date"] = date
            except ValueError:
                logging.error("Geçersiz tarih formatı. YYYY-MM-DD formatında olmalıdır.")
                return None  # Hata durumunda None döndür

        logging.info(f"Lig {league_id} ve sezon {season} için maçlar alınıyor.")
        response = self.api_client.send_request(endpoint, params=params)

        if response and "error" in response:
            logging.error(f"{league_id} ligindeki maçlar alınamadı.")
            return None  # Hata durumunda None döndür

        logging.info(f"{league_id} ligindeki maçlar başarıyla alındı.")
        return response