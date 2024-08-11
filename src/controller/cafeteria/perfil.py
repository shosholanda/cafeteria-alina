from flask import (
    render_template, Blueprint, flash, g, redirect, request, session, url_for
)

# Bibliotecas de seguridad
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import abort


from src.model.repository.repo_usuario import *
from src.model.repository.repo_sucursal import *

from src.controller.auth import admin, requiere_inicio_sesion

from src import db


''' Controlador para las operaciones de producto '''

perfil = Blueprint('perfil', __name__, url_prefix='/perfil') # Crear la sesion


# Ventana perfil
@perfil.route('/')
@requiere_inicio_sesion
def main():
    user = get_usuario(g.user.correo)
    if not user:
        abort(404)
    return render_template('cafeteria/perfil.html', usuario = user)

@perfil.route('/update-usuario/<correo>', methods=['GET', 'POST'])
@requiere_inicio_sesion
def update_usuario(correo):
    user = get_usuario(correo)
    if not user or correo == '':
        flash('Usuario no encontrado')
        return redirect(url_for('perfil.main'))

    if user.id_sucursal:
        user = get_full_usuario(correo)
        
    tipo_usuarios = get_all_tipo_usuario()
    sucursales = get_all_sucursales()
    error = None
    
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellido_paterno = request.form.get('apellido_paterno')
        apellido_materno = request.form.get('apellido_materno')
        fecha_nacimiento = request.form.get('fecha_nacimiento')
        id_tipo_usuario = request.form.get('tipo_usuario')
        id_sucursal = request.form.get('sucursal')
        contraseña_actual = request.form.get('contraseña_actual')
        nueva_contraseña = request.form.get('nueva_contraseña')

        print(nombre, apellido_materno, apellido_paterno, fecha_nacimiento)

        if nombre and apellido_materno and apellido_paterno:
            nombre = nombre.strip().title()
            apellido_paterno = apellido_paterno.strip().title()
            apellido_materno = apellido_materno.strip().title()

        try:
            if nombre and apellido_materno and apellido_paterno and fecha_nacimiento:
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
            flash('Usuario actualizado con éxito!')
            return redirect(url_for('perfil.main'))
        except ValueError:
            flash(error)

    return render_template('cafeteria/crud/update_perfil.html', usuario = user, tipo_usuarios = tipo_usuarios, sucursales = sucursales)


@perfil.route('/delete-usuario/<correo>', methods=['GET', 'POST'])
@admin
def delete_usuario(correo):
    '''Elimina al usuario definitivamente por siempre'''
    user = get_usuario(correo)
    if not user or correo == '':
        flash('Usuario no encontrado')
        return redirect(url_for('perfil.main'))
    
    remove_usuario(user)
    flash('Usuario eliminado con éxito')
    return redirect(url_for('perfil.main'))

