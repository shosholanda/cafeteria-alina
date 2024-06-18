from flask import (
    render_template, Blueprint, flash, g, redirect, request, session, url_for
)

from werkzeug.exceptions import abort

# Create the following databases
from cafeteria_alina.model.producto import Producto

from cafeteria_alina.model.repository.repo_producto import *
from cafeteria_alina.model.repository.repo_tipo_producto import *

from cafeteria_alina.controller.auth import requiere_inicio_sesion


''' Controlador para las operaciones de producto '''

productos = Blueprint('productos', __name__, url_prefix='/productos') # Crear la sesion

# Página de productos de página. EStá afuera de la sesion
@productos.route('/')
@requiere_inicio_sesion
def main():
    productos =get_all_available_productos()
    return render_template('cafeteria/productos.html', productos = productos)


# CREATE PRODUCTO
@productos.route('/agregar-producto', methods=('GET', 'POST'))
@requiere_inicio_sesion
def create_producto():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        descripcion = request.form.get('descripcion')
        #categoria = request.form.get('categoria') maybe in another table

        error = None

        if nombre:
            nombre = nombre.strip().title()
        if descripcion:
            descripcion = descripcion.strip().replace('\n', ' ')

        producto = get_producto(nombre)

        if producto and producto.status == 1:
            error = f'El producto {nombre} ya existe. Indique otro producto'
        elif producto and producto.status == 0:
            producto.status = 1
            producto.descripcion = descripcion
            agregar_producto(producto)
        else:
            producto = Producto(nombre,descripcion)
            agregar_producto(producto)

        if not error:
            return render_template('cafeteria/success.html', tipo = 'Producto', crud = 'agregado')
        flash(error)
    return render_template('cafeteria/crud/create_producto.html', tipo_productos = get_all_available_tipo_producto())

#UPDATE PRODUCTO
@productos.route('/editar-producto/<id>', methods=('GET', 'POST'))
@requiere_inicio_sesion
def update_producto(id):
    producto = get_producto_id(id)
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        descripcion = request.form.get('descripcion')

        error = None
        if not nombre:
            error = 'Se requiere de al menos un nombre'
        if not descripcion or descripcion.strip() == '':
            descripcion = "Sin descripcion"
        
        if error: 
            flash(error)
            return render_template('cafeteria/crud/update_producto.html', producto = producto)

        copy = get_producto(nombre)
        # Si ya existe otro producto con el mismo nombre, mandamos error
        if copy and copy.status == 1:
            error = 'Ya existe otro producto con este mismo nombre:' + str(copy)
        # Si está oculto, lo desbloqueamos sin borrar al anterior producto
        # y dejamos que el usuario decida ocultar el anterior si quiere
        elif copy and copy.status == 0:
            copy.status = 1
            agregar_producto(copy)
        # Uso normal. Escribir bien nombre o descripcion
        else:
            producto.nombre = nombre
            producto.descripcion = descripcion
            agregar_producto(producto)

        if error:
            flash(error)
        else:
            return render_template('cafeteria/success.html', tipo = 'Producto', crud = 'modificado')

    return render_template('cafeteria/crud/update_producto.html', producto = producto)

#DELETE PRODUCTO
@productos.route('/eliminar-producto/<id>')
@requiere_inicio_sesion
def delete_producto(id):
    '''Nunca borramos ningun producto'''
    producto = get_producto_id(id)
    hide_producto(producto)
    return redirect(url_for('productos.main'))


