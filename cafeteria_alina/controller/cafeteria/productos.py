from flask import (
    render_template, Blueprint, flash, g, redirect, request, session, url_for
)

from werkzeug.exceptions import abort

# Create the following databases
from cafeteria_alina.model.producto import Producto

from cafeteria_alina.model.repository.repo_producto import *

from cafeteria_alina.controller.auth import requiere_inicio_sesion


''' Controlador para las operaciones de producto '''

productos = Blueprint('productos', __name__, url_prefix='/productos') # Crear la sesion

# Página de productos de página. EStá afuera de la sesion
@productos.route('/')
@requiere_inicio_sesion
def main():
    productos =read_productos()
    return render_template('cafeteria/productos.html', productos = productos)


# CREATE PRODUCTO
@productos.route('/agregar-producto', methods=('GET', 'POST'))
@requiere_inicio_sesion
def create_producto():
    if request.method == 'POST':

        nombre = request.form.get('nombre')
        descripcion = request.form.get('descripcion')
        if descripcion:
            descripcion = descripcion.strip().replace('\n', ' ')

        id_producto = nombre.strip().lower().replace(' ', '_') 

        producto = get_producto_id(id_producto)
        error = None

        if producto:
            error = f'El producto {id_producto} ya existe. Indique otro producto'
        else:
            producto = Producto(id_producto, nombre, descripcion)
            agregar_producto(producto)
            

        if not error:
            return "Producto registrado exitosamente!"
        else:
            flash(error)
    return render_template('cafeteria/crud/create_producto.html')

#UPDATE PRODUCTO
@productos.route('/editar-producto/<id_prod>', methods=('GET', 'POST'))
@requiere_inicio_sesion
def update_producto(id_prod):
    producto = get_producto_id(id_prod)
    if request.method == 'POST':
        producto.nombre = request.form.get('nombre')
        producto.descripcion = request.form.get('descripcion')

        error = None
        if not producto.nombre:
            error = 'Se requiere de al menos un nombre'
            flash(error)
        else:
            if not producto.descripcion or producto.descripcion.strip() == '':
                producto.descripcion = "Sin descripcion"
            agregar_producto(producto)
            return "Producto modificado con éxito!"

    return render_template('cafeteria/crud/update_producto.html', producto = producto)

#DELETE PRODUCTO
@productos.route('/eliminar-producto/<id_prod>')
@requiere_inicio_sesion
def delete_producto(id_prod):
    producto = get_producto_id(id_prod)
    eliminar_producto(producto)
    return redirect(url_for('productos.main'))



    