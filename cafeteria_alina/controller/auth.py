import functools

from os import error

from flask import (
    render_template, # renderiza el html
    Blueprint, # Registrar la visita a la página 
    flash, # agrega mensajes extra (error principalmente) al html
    g,  # captura si se ha iniciado sesion o no
    redirect, # redireccionar a una ruta
    request,  # para metodos post
    session, # guarda datos de la sesion
    url_for   # endpoints
)

# Bibliotecas de seguridad
from werkzeug.security import generate_password_hash, check_password_hash

#Crear automáticamente las tablas en mysql
from cafeteria_alina.model.usuario import Usuario

# Importar las querys requeridas
from cafeteria_alina.model.repository.repo_usuario import *

''' Controlador para la función de autenticación y registro de usuarios'''

auth = Blueprint('auth', __name__, url_prefix='/auth') # Crear la sesion

# Registrar un usuario
@auth.route('/registrar', methods=['GET', 'POST'])
def registrar_usuario():
    if request.method == 'POST':

        usuario = request.form.get('correo')
        contraseña = request.form.get('contraseña')
        nombre = request.form.get('nombre')
        apellido_paterno = request.form.get('apellido_paterno')
        apellido_materno = request.form.get('apellido_materno')
        fecha_nacimiento = request.form.get('fecha_nacimiento')


        user = Usuario(usuario, generate_password_hash(contraseña), nombre, apellido_paterno, apellido_materno, fecha_nacimiento)

        error = None

        if not usuario:
            error = 'Se requiere nombre de usuario'
        if not contraseña:
            error = 'Se requere una contraseña'


        if not get_usuario(usuario):
            crear_usuario(user)

        else: 
            error = 'Usuario ya existe'

        
        
        
        if error != None:
            flash(error)
    return render_template('auth/register.html')






