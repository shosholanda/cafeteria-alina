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
@auth.route('/registrar-usuario', methods=['GET', 'POST'])
def registrar_usuario():
    if request.method == 'POST':

        usuario = request.form.get('correo')
        contraseña = request.form.get('contraseña')
        nombre = request.form.get('nombre')
        apellido_paterno = request.form.get('apellido_paterno')
        apellido_materno = request.form.get('apellido_materno')
        fecha_nacimiento = request.form.get('fecha_nacimiento')



        error = None

        if not usuario:
            error = 'Se requiere nombre de usuario'
        if not contraseña:
            error = 'Se requere una contraseña'


        if not get_usuario(usuario):
            user = Usuario(usuario, generate_password_hash(contraseña), nombre, apellido_paterno, apellido_materno, fecha_nacimiento)
            crear_usuario(user)

        else: 
            error = 'Usuario ya existe'
        
        if error != None:
            flash(error)
        else:
            return "Usuario registrado correctamente" #redirect(url_for('inicio.main'))
    return render_template('auth/register.html')


# Iniciar sesion
@auth.route('/iniciar-sesion', methods=['GET', 'POST'])
def iniciar_sesion():
    if request.method == 'POST':

        usuario = request.form.get('correo')
        contraseña = request.form.get('contraseña')
        error = None

        if not usuario:
            error = 'Se requiere nombre de usuario'
        if not contraseña:
            error = 'Se requere una contraseña'
        
        user = get_usuario(usuario)

        if user == None or not check_password_hash(user.contraseña, contraseña):
            error = 'Usuario o contraseña incorrecta'

    
        if error is None:
            session.clear()
            session['usuario'] = user.correo
            return redirect(url_for('inicio.main'))
        else:
            flash(error)

    return render_template('auth/login.html')


# Verificación de inicio de sesion
@auth.before_app_request
def cargar_usuarios_logeados():
    usuario = session.get('usuario')
    if not usuario:
        g.user = None
    else:
        g.user = Usuario.query.get(usuario)


# Cerrar sesion
@auth.route('/cerrar-sesion')
def cerrar_sesion():
    session.clear()
    return redirect(url_for('home'))

# REquerir inicio de sesion
def requiere_inicio_sesion(vista):
    @functools.wraps(vista)
    def vista_wraped(**kwargs):
        if g.user is None:
            return redirect(url_for('home'))
        return vista(**kwargs)
    return vista_wraped
