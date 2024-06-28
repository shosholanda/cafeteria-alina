from flask import (
    render_template, Blueprint, flash, g, redirect, request, session, url_for
)

# Bibliotecas de seguridad
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import abort


from cafeteria_alina.model.repository.repo_usuario import *
from cafeteria_alina.model.repository.repo_sucursal import *

from cafeteria_alina.controller.auth import requiere_inicio_sesion

from cafeteria_alina import db


''' Controlador para las operaciones de producto '''

perfil = Blueprint('perfil', __name__, url_prefix='/perfil') # Crear la sesion


# Ventana perfil
@perfil.route('/')
@requiere_inicio_sesion
def main():
    user = get_usuario(g.user.correo)
    if not user:
        return redirect(url_for('inicio.main'))
    return render_template('cafeteria/perfil.html', usuario = user)

@perfil.route('/update-usuario', methods=['GET', 'POST'])
@requiere_inicio_sesion
def update_usuario():
    user = get_usuario(g.user.correo)

    if user.id_sucursal:
        user = get_full_usuario(g.user.correo)
        
    tipo_usuarios = get_all_tipo_usuario()
    sucursales = get_all_sucursales()

    error = None
    msg = ''
    
    if request.method == 'POST':
        nombre = request.form.get('nombre').strip()
        apellido_paterno = request.form.get('apellido_paterno').strip()
        apellido_materno = request.form.get('apellido_materno').strip()
        fecha_nacimiento = request.form.get('fecha_nacimiento').strip()
        id_tipo_usuario = request.form.get('tipo_usuario')
        id_sucursal = request.form.get('sucursal')
        contraseña_actual = request.form.get('contraseña_actual')
        nueva_contraseña = request.form.get('nueva_contraseña')

        try:
            user.nombre = nombre
            user.apellido_paterno = apellido_paterno
            user.apellido_materno = apellido_materno
            user.fecha_nacimiento = fecha_nacimiento
            if id_tipo_usuario:
                id_tipo_usuario = int(id_tipo_usuario)
                user.id_tipo_usuario = id_tipo_usuario
            if id_sucursal:
                id_sucursal = int(id_sucursal)
                user.id_sucursal = id_sucursal
            
            if nueva_contraseña and contraseña_actual:
                if not check_password_hash(user.contraseña, contraseña_actual):
                    error = 'La contraseña actual con coincide con su actual contraseña'
                    raise Exception()
                else:
                    nueva_contraseña = generate_password_hash(nueva_contraseña)
                    user.contraseña = nueva_contraseña

            add_usuario(user)
            return render_template('cafeteria/success.html', tipo = 'Perfil', crud= 'actualizado')
        except ValueError:
            if not error :
                error = 'no se registró bien el tipo usuario o sucursal'

        if error:
            flash(error)
        

    return render_template('cafeteria/crud/update_perfil.html', usuario = user, tipo_usuarios = tipo_usuarios, sucursales = sucursales)