import os
import logging

class Config:
    api_url = os.getenv('API_URL', "https://v3.football.api-sports.io")
    api_key = os.getenv('API_KEY')
    db_path = os.getenv('DATABASE_URL', 'sqlite:///database.db')  # SQLite veritabanı yolu

    @staticmethod
    def check_env_variables():
        if not Config.api_url:
            raise ValueError("API URL ortam değişkeni eksik. Lütfen ortam değişkenlerini kontrol edin.")
        logging.info("API URL başarıyla okundu.")

        if not Config.api_key:
            raise ValueError("API Key ortam değişkeni eksik. Lütfen ortam değişkenlerini kontrol edin.")
        logging.info("API Key başarıyla okundu.")

        if not Config.db_path:
            raise ValueError("Veritabanı yolu ortam değişkeni eksik. Lütfen ortam değişkenlerini kontrol edin.")
        logging.info("Veritabanı yolu başarıyla okundu.")