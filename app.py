from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)
annio = datetime.now().year

@app.route('/')
def index():
    return render_template('index.html', titulo = "User's Page", titulo_banner = "Home", annio = annio)

@app.route('/registrar')
def registrar():
    return render_template('registro.html', titulo = "User's Page", titulo_banner = "Registration", annio = annio)

@app.route('/acceder')
def acceder():
    return render_template('acceso.html', titulo = "User's Page", titulo_banner = "Loggin In", annio = annio)

if __name__ == "__main__":
    app.run(debug=True)