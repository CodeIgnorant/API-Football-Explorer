import logging
from app.api.api_client import APIClient

class Standings:
    def __init__(self, api_client: APIClient):
        self.api_client = api_client

    def get_standings_league_season(self, league_id, season):
        """Belirli bir lig ve sezona göre sıralamaları almak için kullanılan metod."""
        if not isinstance(league_id, int) or league_id <= 0:
            logging.error("Geçersiz lig ID'si. Pozitif bir tam sayı olmalıdır.")
            return None  # Hata durumunda None döndür

        if not isinstance(season, int) or not (1000 <= season <= 9999):
            logging.error("Geçersiz sezon. Yıl formatında (YYYY) olmalıdır.")
            return None  # Hata durumunda None döndür

        endpoint = "standings"
        params = {
            "league": league_id,
            "season": season
        }
        logging.info(f"{league_id} ligindeki {season} sezonunun sıralamaları alınıyor.")
        response = self.api_client.send_request(endpoint, params=params)

        if response and "error" in response:
            logging.error(f"{league_id} ligindeki {season} sezonu için sıralamalar alınamadı.")
            return None  # Hata durumunda None döndür

        logging.info(f"{league_id} ligindeki {season} sezonunun sıralamaları başarıyla alındı.")
        return response
