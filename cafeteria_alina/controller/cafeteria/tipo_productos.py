from flask import (
    render_template, Blueprint, flash, g, redirect, request, session, url_for
)

from werkzeug.exceptions import abort

from cafeteria_alina.model.repository.repo_tipo_producto import *

from cafeteria_alina.controller.auth import requiere_inicio_sesion


''' Controlador para las operaciones de producto '''

tipo_productos = Blueprint('tipo-productos', __name__, url_prefix='/tipo-productos') # Crear la sesion

# Página de tipo_productos de página. EStá afuera de la sesion
@tipo_productos.route('/')
@requiere_inicio_sesion
def main():
    tipo_productos = get_all_available_tipo_producto()
    return render_template('cafeteria/tipo_productos.html', tipo_productos = tipo_productos)


# CREATE PRODUCTO
@tipo_productos.route('/agregar-tipo', methods=('GET', 'POST'))
@requiere_inicio_sesion
def create_tipo():
    tipo_productos = get_all_available_tipo_producto()
    if request.method == 'POST':
        nuevo_tipo = request.form.get('tipo')
        error = None
        if nuevo_tipo is None:
           error = 'Agregue un nombre significativo'
        
        nuevo_tipo = nuevo_tipo.strip().upper()
        tipo = get_by_tipo(nuevo_tipo)
        if not tipo:
            tipo = TipoProducto(nuevo_tipo)
            crear_tipo_producto(tipo)
        elif tipo.status == 0:
            tipo.status = 1
            crear_tipo_producto(tipo)
        else:
            error = 'El tipo ya existe!'

        if not error:
            return render_template('cafeteria/success.html', tipo = 'Producto', crud = 'agregado')
        else:
            flash(error)


    return render_template('cafeteria/crud/create_tipo_producto.html', tipo_productos = tipo_productos)

#UPDATE PRODUCTO
@tipo_productos.route('/editar-producto/<id>', methods=('GET', 'POST'))
@requiere_inicio_sesion
def update_tipo(id):
    # producto = get_producto_id(id)
    # if request.method == 'POST':
    #     producto.nombre = request.form.get('nombre')
    #     producto.descripcion = request.form.get('descripcion')

    #     error = None
    #     if not producto.nombre:
    #         error = 'Se requiere de al menos un nombre'
    #         flash(error)
    #     else:
    #         if not producto.descripcion or producto.descripcion.strip() == '':
    #             producto.descripcion = "Sin descripcion"
    #         agregar_producto(producto)
    #         return render_template('cafeteria/success.html', tipo = 'Producto', crud = 'modificado')

    # return render_template('cafeteria/crud/update_producto.html', producto = producto)
    return "Aquí editamos" + id

#DELETE PRODUCTO
@tipo_productos.route('/eliminar-producto/<id>')
@requiere_inicio_sesion
def delete_tipo(id):
    # producto = get_producto_id(id)
    # remove_producto(producto)
    # return redirect(url_for('tipo_productos.main'))
    return "Aquí eliminamos el producto " +id

