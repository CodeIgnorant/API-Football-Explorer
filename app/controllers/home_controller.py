from flask import render_template
from app import app  # Eğer bir app nesnesi oluşturduysan, bu dosya burada tanımlı olmalı.

@app.route('/')
def home():
    return render_template('index.html')  # templates/index.html dosyasını render et