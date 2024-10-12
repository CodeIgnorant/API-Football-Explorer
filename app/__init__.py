from flask import Flask
import os
import logging

# Flask uygulamasını başlat
app = Flask(__name__)

# Config dosyasını yükle
app.config.from_object('app.settings.config.Config')

# Logging yapılandırması ekleyelim
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Controller'ları dahil et
from app.controllers import (
    test_api_controller,  # Test API ile ilgili controller
    countries_controller,  # Ülkeler ile ilgili controller
    home_controller        # Ana sayfa ile ilgili controller (yeni eklenen)
)
