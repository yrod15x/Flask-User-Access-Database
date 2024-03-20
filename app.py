from flask import Flask, render_template, redirect, url_for, request
from datetime import datetime
from formularios import FormAcceso, FormRegistro

app = Flask(__name__)
annio = datetime.now().year

app.config['SECRET_KEY'] = 'ABC1234'

@app.route('/')
def index():
    return render_template('index.html', titulo = "User's Page", titulo_banner = "Home", annio = annio)

@app.route('/registrar', methods = ['POST', 'GET'])
def registrar():
    #Instancia de clase que permite usar los elementos del formulario
    formulario = FormRegistro()
    #Si el usuario escribio bien los campos lo regresa a la pagina de inicio
    if formulario.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('registro.html', titulo = "User's Page", titulo_banner = "Registration", annio = annio, formulario = formulario)

@app.route('/acceder')
def acceder():
    formulario = FormAcceso()
    return render_template('acceso.html', titulo = "User's Page", titulo_banner = "Loggin In", annio = annio, formulario = formulario)

if __name__ == "__main__":
    app.run(debug=True)