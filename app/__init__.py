from flask import Flask
import logging

# Flask uygulamasını başlat
app = Flask(__name__)

# Config dosyasını yükle
app.config.from_object('app.settings.config.Config')

# Logging yapılandırması ekleyelim
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Controller'ları dahil et
from app.controllers import *  # Tüm controller'ları tek seferde içe aktar
