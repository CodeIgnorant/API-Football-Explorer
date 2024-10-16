from app import db

class Country(db.Model):
    __tablename__ = 'countries'  # Table name in the database

    id = db.Column(db.Integer, primary_key=True)  # Primary key
    name = db.Column(db.String(30), nullable=False)  # Country name (30 characters)
    code = db.Column(db.String(10), nullable=False)  # Country code
    flag = db.Column(db.String(255), nullable=True)  # Flag URL
    last_updated = db.Column(db.DateTime, nullable=True)  # Last updated date

    def __repr__(self):
        return f'<Country {self.name} ({self.code})>'  # Basic representation