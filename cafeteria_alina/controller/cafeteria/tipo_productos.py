from flask import (
    render_template, Blueprint, flash, g, redirect, request, session, url_for
)

from werkzeug.exceptions import abort

from cafeteria_alina.model.repository.repo_tipo_producto import *

from cafeteria_alina.controller.auth import requiere_inicio_sesion, admin


''' Controlador para las operaciones de producto '''

tipo_productos = Blueprint('tipo-productos', __name__, url_prefix='/tipo-productos') # Crear la sesion

# Página de tipo_productos de página. EStá afuera de la sesion
@tipo_productos.route('/')
@requiere_inicio_sesion
@admin
def main():
    tipo_productos = get_all_available_tipo_producto()
    return render_template('cafeteria/tipo_productos.html', tipo_productos = tipo_productos)


# CREATE PRODUCTO
@tipo_productos.route('/agregar-tipo', methods=('GET', 'POST'))
@requiere_inicio_sesion
@admin
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
            flash('tipo de producto agregado!')
            return redirect(url_for('tipo-productos.create_tipo'))
        else:
            flash(error)


    return render_template('cafeteria/crud/create_tipo_producto.html', tipo_productos = tipo_productos)

