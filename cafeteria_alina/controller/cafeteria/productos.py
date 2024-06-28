from flask import (
    render_template, Blueprint, flash, g, redirect, request, session, url_for
)

from werkzeug.exceptions import abort

# Create the following databases
from cafeteria_alina.model.producto import Producto

from cafeteria_alina.model.repository.repo_producto import *
from cafeteria_alina.model.repository.repo_tipo_producto import *
from cafeteria_alina.model.repository.repo_categoria import *
from cafeteria_alina.model.repository.repo_usuario import *

from cafeteria_alina.controller.auth import requiere_inicio_sesion
from cafeteria_alina.controller.auth import admin


''' Controlador para las operaciones de producto '''

productos = Blueprint('productos', __name__, url_prefix='/productos') # Crear la sesion

# Página de productos de página. EStá afuera de la sesion
@productos.route('/')
@requiere_inicio_sesion
def main():
    user = get_usuario(g.user.correo)
    productos =get_all_available_productos()
    return render_template('cafeteria/productos.html', productos = productos, usuario = user)


# CREATE PRODUCTO
@productos.route('/agregar-producto', methods=('GET', 'POST'))
@requiere_inicio_sesion
@admin
def create_producto():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        descripcion = request.form.get('descripcion')
        categoria = request.form.get('categoria')

        error = None

        if nombre and categoria:
            nombre = nombre.strip().title()
        else:
            error = 'Se requiere de nombre y categoria'
        if descripcion:
            descripcion = descripcion.strip().replace('\n', ' ')
        else: 
            descripcion = 'Sin descripcion'

        if error: 
            flash(error)
            return render_template('cafeteria/crud/create_producto.html', categorias = get_all_categorias())

        # Pueden haber productos de diferentes categorias
        # chocolate - caliente
        # chocolate - smoothiee
        producto = get_producto_and_categoria(nombre, int(categoria))

        if producto and producto.status == 1:
            error = f'El producto {nombre} ya existe. Indique otro producto'
        elif producto and producto.status == 0:
            producto.status = 1
            producto.descripcion = descripcion
            agregar_producto(producto)
        else:
            producto = Producto(nombre,descripcion, int(categoria))
            agregar_producto(producto)

        if not error:
            flash('Producto añadido correctamente!')
            return redirect(url_for('productos.create_producto'))
        flash(error)
    return render_template('cafeteria/crud/create_producto.html', categorias = get_all_categorias())

#UPDATE PRODUCTO
@productos.route('/editar-producto/<int:id_producto>', methods=('GET', 'POST'))
@requiere_inicio_sesion
@admin
def update_producto(id_producto): 
    producto = get_producto_id(id_producto)
    categorias = get_all_categorias()
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        descripcion = request.form.get('descripcion')
        categoria = request.form.get('categoria')

        error = None
        if not nombre:
            error = 'Se requiere de al menos un nombre'
        if not descripcion or descripcion.strip() == '':
            descripcion = "Sin descripcion"
        if not categoria:
            error = 'Se requiere de al menos alguna categoria para clasificar este producto'
        
        if error: 
            flash(error)
            return render_template('cafeteria/crud/update_producto.html', producto = producto, categorias = categorias)

        # No pueden haber 2 con el mismo nombre y categoria
        copy = get_producto_and_categoria(nombre, int(categoria))
        
        # Reemplazamos si no hay o si es el mismo
        if copy is None or copy.id == producto.id:
            producto.nombre = nombre
            producto.descripcion = descripcion
            producto.id_categoria = int(categoria)
            producto.status = 1
            agregar_producto(producto)

        else: #Ya existe un nombre igual
            if copy.status == 1:
                error = 'Ya existe un producto con ese nombre: ' + str(copy)
            else:
                # Actualizamos el q estaba "eliminado"
                # Y dejamos el original intacto, que lo elimine el usuario
                copy.nombre = nombre
                copy.descripcion = descripcion
                copy.id_categoria = int(categoria)
                copy.status == 1
                agregar_producto(copy)

        if error:
            flash(error)
        else:
            flash('Producto modificado con éxito!')
            return redirect(url_for('productos.main'))

    return render_template('cafeteria/crud/update_producto.html', producto = producto, categorias = categorias)

#DELETE PRODUCTO
@productos.route('/eliminar-producto/<id_producto>')
@requiere_inicio_sesion
@admin
def delete_producto(id_producto):
    '''Nunca borramos ningun producto'''
    producto = get_producto_id(id_producto)
    hide_producto(producto)
    return redirect(url_for('productos.main'))


