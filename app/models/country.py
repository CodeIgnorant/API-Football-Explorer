from app import db

class Country(db.Model):
    __tablename__ = 'countries'  # Veritabanındaki tablo adı

    id = db.Column(db.Integer, primary_key=True)  # Birincil anahtar
    name = db.Column(db.String(30), nullable=False)  # Ülke adı (30 karakter)
    code = db.Column(db.String(10), nullable=False)  # Ülke kodu
    flag = db.Column(db.String(255), nullable=True)  # Bayrak URL'si
    last_updated = db.Column(db.DateTime, nullable=True)  # Son güncelleme tarihi

    def __repr__(self):
        return f'<Country {self.name} ({self.code})>'  # Temel temsil
