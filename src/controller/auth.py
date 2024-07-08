import functools

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
from src.model.usuario import Usuario

# Importar las querys requeridas
from src.model.repository.repo_usuario import *

''' Controlador para la función de autenticación y registro de usuarios'''

auth = Blueprint('auth', __name__, url_prefix='/auth') # Crear la sesion

# Registrar un usuario
@auth.route('/registrar-usuario', methods=['GET', 'POST'])
def registrar_usuario():
    if request.method == 'POST':
        correo = request.form.get('correo')
        contraseña = request.form.get('contraseña')
        nombre = request.form.get('nombre').strip().title()
        apellido_paterno = request.form.get('apellido_paterno').strip().title()
        apellido_materno = request.form.get('apellido_materno').strip().title()
        fecha_nacimiento = request.form.get('fecha_nacimiento')
        error = None

        if not correo:
            error = 'Se requiere nombre de usuario'
        if not contraseña:
            error = 'Se requere una contraseña'
        if not get_usuario(correo):
            user = Usuario(correo=correo,
                           contraseña=generate_password_hash(contraseña),
                           nombre=nombre,
                           apellido_paterno=apellido_paterno,
                           apellido_materno=apellido_materno,
                           id_tipo_usuario=1,
                           id_sucursal=None,
                           fecha_nacimiento=fecha_nacimiento)
            add_usuario(user)
        else: 
            error = 'Usuario ya existe'
        if error != None:
            flash(error, 'error')
        else:
            return render_template('cafeteria/success.html')
    return render_template('auth/register.html')


# Iniciar sesion
@auth.route('/iniciar-sesion', methods=['GET', 'POST'])
def iniciar_sesion():
    if request.method == 'POST':

        usuario = request.form.get('correo')
        contraseña = request.form.get('contraseña')
        error = None
        
        user = get_usuario(usuario)
        
        if not user or not check_password_hash(user.contraseña, contraseña):
            error = 'Usuario o contraseña incorrecta'
        
        elif user.status == 0:
            error = 'Cuenta de usuario suspendida'
    
        if error is None:
            session.clear()
            session['usuario'] = user.correo
            session['sucursal'] = user.id_sucursal
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
        user = get_usuario_and_tipo(usuario)
        g.user = user


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

# Es un admin
def admin(vista):
    @functools.wraps(vista)
    def vista_wraped(**kwargs):
        if not g.user:
            return redirect(url_for('home'))
        if not 'ADMIN' in g.user.tipo_usuario.nombre.upper():
            return redirect(url_for('inicio.main'))
        return vista(**kwargs)
    return vista_wraped
