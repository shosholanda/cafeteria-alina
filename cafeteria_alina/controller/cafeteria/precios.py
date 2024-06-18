from flask import (
    render_template, Blueprint, flash, g, redirect, request, session, url_for
)

from werkzeug.exceptions import abort

from cafeteria_alina.model.repository.repo_producto import *
from cafeteria_alina.model.repository.repo_tipo_producto import *

from cafeteria_alina.controller.auth import requiere_inicio_sesion


''' Controlador para las operaciones de precio '''

precios = Blueprint('precios', __name__, url_prefix='/precios') # Crear la sesion

# Página de precio de página. EStá afuera de la sesion
@precios.route('/')
@requiere_inicio_sesion
def main():
    precios = get_all_avaliable_precios()
    return render_template('cafeteria/precios.html', precios = precios)


# CREATE PRECIO
@precios.route('/agregar-precio/<id>', methods=('GET', 'POST'))
@requiere_inicio_sesion
def create_precio(id):
    producto = get_producto_id(id)
    precios = get_all_available_tipo_producto()
    if request.method == 'POST':
        tipo = request.form.get('tipo')
        
        error = None
        try:
            precio = float(request.form.get('precio'))
            nuevo_precio = get_precio_unico(id, tipo)
            if nuevo_precio and nuevo_precio.status == 1:
                error = 'Ya existe esta asignación'
        except ValueError:
            error = 'No se ha ingresado un precio válido. Ej. 14.22'

        if error:
            flash(error)
        else:
            if nuevo_precio and nuevo_precio.status == 0:
                nuevo_precio.status = 1
                precio = nuevo_precio
            else:
                precio = Precio(id, tipo, precio)
            add_precio(precio)
            return render_template('cafeteria/success.html', tipo = 'Producto', crud = 'agregado', obj = precio)
        
    return render_template('cafeteria/crud/create_precio.html', producto = producto, precios = precios)

#UPDATE PRECIO
@precios.route('/editar-precio/<id>%<tipo>', methods=('GET', 'POST'))
@requiere_inicio_sesion
def update_precio(id, tipo):
    # Siempre va a existir porque no saldría el endpoint
    precio_existente = get_precio_unico(id, tipo)
    tipos = get_all_available_tipo_producto()
    if request.method == 'POST':
        tipo = request.form.get('tipo')
        precio = request.form.get('precio')
        
        error = None
        try:
            precio = float(precio)
            tipo = int(tipo)
        except ValueError:
            error = 'No se ha ingresado un precio válido. Ej. 14.22'
        
        if not error:

            copy = get_precio_unico(id, tipo)
            # Si ya existe el producto al q vamos a modificar
            # y esta oculto (o no), lo desbloqueamos y actualizamos
            # El último registro es eliminado
            if copy :
                remove_precio(copy)
            precio_existente.id_tipo = tipo
            precio_existente.precio = precio
            add_precio(precio_existente)
            return render_template('cafeteria/success.html', tipo = 'Producto', crud = 'actualizado', obj = precio)
        else:
            flash(error)


    return render_template('cafeteria/crud/update_precio.html', precio = precio_existente, tipos = tipos)

#DELETE PRECIO
@precios.route('/eliminar-precio/<id>%<tipo>')
@requiere_inicio_sesion
def delete_precio(id, tipo):
    '''Soft delete precio'''
    precio = get_precio_unico(id, tipo)
    hide_precio(precio)
    return redirect(url_for('productos.main'))
    