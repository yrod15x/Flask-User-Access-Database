#Permite la conversión de codigo python en html
from flask_wtf import FlaskForm
#Permite agregar los elementos (etiquetas) de un formulario
from wtforms import StringField, PasswordField, SubmitField
#Permite agregar validaciones a las etiquetas del formulario
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired

class FormRegistro(FlaskForm):
    """Cada formulario se hace en base a una casa para su posterior instanciamiento en los archivos HTML. Estas clases heredan las variables y metodos de la clas FlaskForm"""
    nom_usuario = StringField('Nombre Usuario', validators = [DataRequired(), Length(min=4, max= 20)])
    correo = StringField(label=('Email'), validators = [DataRequired(), Email()])
    contrasena = PasswordField('Contraseña', validators = [DataRequired()])
    rep_contrasena = PasswordField('Confirme Contraseña', validators=[DataRequired(), EqualTo('contrasena')])
    btn_registrar = SubmitField('Registrar')
    
class FormAcceso(FlaskForm):
    correo = StringField('Email', validators = [DataRequired(), Email()])
    contrasena = PasswordField('Contraseña', validators = [DataRequired()])
    btn_acceder = SubmitField('Acceder')
