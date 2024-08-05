from flask import (
    render_template, Blueprint, flash, g, redirect, request, session, url_for
)

from werkzeug.exceptions import abort

from src.model.repository.repo_tipo_producto import *

from src.controller.auth import requiere_inicio_sesion, admin


''' Controlador para las operaciones de producto '''

tipo_productos = Blueprint('tipo-productos', __name__, url_prefix='/tipo-productos') # Crear la sesion

# Página de tipo_productos de página. EStá afuera de la sesion
@tipo_productos.route('/')
@requiere_inicio_sesion
@admin
def main():
    # AAA Hay que revisar bien los status!
    tipo_productos = get_all_tipo_producto()
    return render_template('cafeteria/tipo_productos.html', tipo_productos = tipo_productos)


# CREATE 
@tipo_productos.route('/agregar-tipo', methods=('GET', 'POST'))
@requiere_inicio_sesion
@admin
def create_tipo():
    all_tipos = get_all_tipo_producto()
    error = None
    if request.method == 'POST':
        nuevo_tipo = request.form.get('tipo')
        if not nuevo_tipo or nuevo_tipo.strip() == '':
           error = 'Agregue un nombre significativo'
           flash(error)
           return redirect(url_for('tipo-producto.create_tipo'))
        
        nuevo_tipo = nuevo_tipo.strip().upper()
        tipo = get_by_tipo(nuevo_tipo)
        if not tipo:
            tipo = TipoProducto(nuevo_tipo)
            add_tipo_producto(tipo)
        elif tipo.status == 0:
            tipo.status = 1
            add_tipo_producto(tipo)
        else:
            error = 'El tipo ya existe!'

        if not error:
            flash('tipo de producto agregado!')
            return redirect(url_for('tipo-productos.create_tipo'))
        flash(error)

    return render_template('cafeteria/crud/create_tipo_producto.html', tipo_productos = all_tipos)


# UPDATE PRODUCTO
@tipo_productos.route('/editar-tipo/<int:id_tipo_producto>', methods=('GET', 'POST'))
@requiere_inicio_sesion
@admin
def update_tipo(id_tipo_producto):
    all_tipos = get_all_tipo_producto()
    tipo = get_by_id(id_tipo_producto)
    if not tipo:
        abort(404)
    
    if request.method == 'POST':
        nuevo_tipo = request.form.get('tipo')
        status = request.form.get('status')

        status = True if status else 0

        error = None
        if not nuevo_tipo or nuevo_tipo.strip() == '':
           error = 'Agregue un nombre significativo'
           flash(error)
           return redirect(url_for('tipo-producto.update_tipo', id_tipo_producto = id_tipo_producto))
        
        nuevo_tipo = nuevo_tipo.strip().upper()
        tipo = get_by_tipo(nuevo_tipo)
        tipo.status = status
        if tipo:
            error = 'El tipo ya existe! Especifique otro nombre'
        else:
            add_tipo_producto(tipo)

        if not error:
            flash('tipo de producto modificado!')
            return redirect(url_for('tipo-productos.create_tipo'))
        flash(error)

    return render_template('cafeteria/crud/update_tipo_producto.html', tipo_producto = tipo, tipo_productos = all_tipos)



# DELETE PRODUCTO
@tipo_productos.route('/delete-tipo/<int:id_tipo_producto>', methods=('GET', 'POST'))
@requiere_inicio_sesion
@admin
def delete_tipo(id_tipo_producto):
    tipo = get_by_id(id_tipo_producto)
    if not tipo:
        abort(404)
    tipo.status = 0
    add_tipo_producto(tipo)
    return redirect(url_for('tipo-productos.create_tipo'))