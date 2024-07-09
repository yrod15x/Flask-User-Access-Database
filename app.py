from flask import Flask, render_template, redirect, url_for, request, flash
from datetime import datetime
from formularios import FormAcceso, FormRegistro
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
annio = datetime.now().year

app.config['SECRET_KEY'] = 'ABC1234'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nom_user = db.Column(db.String(20), nullable = False)
    correo = db.Column(db.String(50), unique = True, nullable = False)
    contrasena = db.Column(db.String(32), nullable = False)

@app.route('/')
def index():
    return render_template('index.html', titulo = "User's Page", titulo_banner = "Home", annio = annio)

@app.route('/registrar', methods = ['POST', 'GET'])
def registrar():
    #Instancia de clase que permite usar los elementos del formulario
    formulario = FormRegistro()
    #Si el usuario escribio bien los campos lo regresa a la pagina de inicio
    if formulario.validate_on_submit():
        #Llenar la base de datos con la informacion que viene del formulario
        #Verificar que el email (nombre de usuraio) no este registrado en BD (sea unico)
        usuario = Usuario.query.filter_by(correo = formulario.correo.data).first()
        #si el email no esta registrado, registrar todos los datos en la BD
        if usuario is None:
            #Crear un objeto tipo BD que contenga la informacion del formulario
            usuario = Usuario(nom_user = formulario.nom_usuario.data, 
            correo = formulario.correo.data,contrasena = formulario.contrasena.data)
            #Agregar la informacion a la BD
            db.session.add(usuario)
            db.session.commit()
            #limpiar los campos del formulario para el proximo registro
            formulario.nom_usuario.data = ''
            formulario.correo.data = ''
            formulario.contrasena.data = ''
            flash("Usario Agregado Exitosamente")
            
        #Esto es para debug ' Si ne en verdad se registro la info
        #users = Usuario.query.order_by(Usuario.nom_user) 
        #for user in users:
            #print(f"{user.nom_user} --> {user.correo}")
            
        return redirect(url_for('index'))
    return render_template('registro.html', titulo = "User's Page", titulo_banner = "Registration", annio = annio, formulario = formulario)

@app.route('/acceder', methods = ['POST', 'GET'])
def acceder():
    formulario = FormAcceso()
    #tomo los datos del formulario que voy a validar
    correo = formulario.correo.data
    contrasena = formulario.contrasena.data
    if formulario.validate_on_submit():
        #Busco en la base de datos si el correo ingresado esta en la db
        usuario = Usuario.query.filter_by(correo = formulario.correo.data).first()
        #Si ya esta registrado comparo si la contrasena y el correo son iguales en db
        if usuario is not None:
            if correo == usuario.correo and contrasena == usuario.contrasena:
                flash("Acceso Permitido")
                return render_template('user.html', titulo = "User's Page")
            else:
                flash("Usuario No Registrado")
                return redirect(url_for('index'))
    return render_template('acceso.html', titulo = "User's Page", titulo_banner = "Loggin In", annio = annio, formulario = formulario)

if __name__ == "__main__":
    app.run(debug=True)