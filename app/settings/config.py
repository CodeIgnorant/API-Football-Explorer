import os
import logging
import re

class Config:
    api_url = os.getenv('API_URL', "https://v3.football.api-sports.io")
    api_key = os.getenv('API_KEY')
    db_path = os.getenv('DATABASE_URL', 'sqlite:///database.db')  # SQLite veritabanı yolu

    @staticmethod
    def check_env_variables():
        if not Config.api_url:
            logging.error("API URL ortam değişkeni eksik. Lütfen ortam değişkenlerini kontrol edin.")
            raise ValueError("API URL ortam değişkeni eksik.")
        
        if not re.match(r'^https?://', Config.api_url):
            logging.error("Geçersiz API URL formatı.")
            raise ValueError("Geçersiz API URL formatı.")

        logging.info("API URL başarıyla okundu.")

        if not Config.api_key:
            logging.error("API Key ortam değişkeni eksik. Lütfen ortam değişkenlerini kontrol edin.")
            raise ValueError("API Key ortam değişkeni eksik.")
        logging.info("API Key başarıyla okundu.")

        if not Config.db_path:
            logging.error("Veritabanı yolu ortam değişkeni eksik. Lütfen ortam değişkenlerini kontrol edin.")
            raise ValueError("Veritabanı yolu ortam değişkeni eksik.")
        logging.info("Veritabanı yolu başarıyla okundu.")
