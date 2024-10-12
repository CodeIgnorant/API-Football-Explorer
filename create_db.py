import logging
from app import db
from app.models import *  # Tüm modelleri içe aktar

# Logging yapılandırması
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_database():
    try:
        db.create_all()  # Tüm tanımlı modeller için tabloları oluştur
        logging.info("Veritabanı ve tablolar başarıyla oluşturuldu.")
    except Exception as e:
        logging.error(f"Veritabanı oluşturulurken bir hata meydana geldi: {e}")

if __name__ == "__main__":
    create_database()  # Script çalıştırıldığında veritabanını oluştur