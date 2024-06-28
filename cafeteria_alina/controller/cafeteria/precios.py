from flask import (
    render_template, Blueprint, flash, g, redirect, request, session, url_for
)

from werkzeug.exceptions import abort

from cafeteria_alina.model.repository.repo_precio import *
from cafeteria_alina.model.repository.repo_producto import *
from cafeteria_alina.model.repository.repo_tipo_producto import *

from cafeteria_alina.controller.auth import requiere_inicio_sesion, admin


''' Controlador para las operaciones de precio '''

precios = Blueprint('precios', __name__, url_prefix='/precios') # Crear la sesion

# Página de precio de página. EStá afuera de la sesion
@precios.route('/')
@requiere_inicio_sesion
@admin
def main():
    precios = get_all_avaliable_precios_by('NOMBRE')
    productos = get_all_available_productos()
    return render_template('cafeteria/precios.html', precios = precios, productos = productos)


# CREATE PRECIO
@precios.route('/agregar-precio/<id_producto>', methods=('GET', 'POST'))
@requiere_inicio_sesion
@admin
def create_precio(id_producto):
    '''Crea un nuevo precio para el producto <id_producto>'''
    producto = get_producto_id(id_producto)
    if not producto:
        return "No se ha podido cargar el producto " + id_producto
    
    tipos = get_all_tipo_producto()
    if request.method == 'POST':
        id_tipo_producto = request.form.get('tipo')
        
        error = None
        try:
            precio = float(request.form.get('precio'))
            nuevo_precio = get_precio_unico(id_producto, id_tipo_producto)
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
                precio = Precio(id_producto = id_producto,
                                id_categoria= 1, 
                                id_tipo_producto=id_tipo_producto, 
                                precio = precio)
            add_precio(precio)
            flash('Precio para ' + producto.nombre + ' creado con éxito!')
            return redirect(url_for('productos.main'))
        
    return render_template('cafeteria/crud/create_precio.html', producto = producto, tipos = tipos)

#UPDATE PRECIO
@precios.route('/editar-precio/<id_producto>%<id_tipo_producto>', methods=('GET', 'POST'))
@requiere_inicio_sesion
@admin
def update_precio(id_producto, id_tipo_producto):
    # Siempre va a existir porque no saldría el endpoint
    precio_existente = get_precio_unico(id_producto, id_tipo_producto)
    if precio_existente and precio_existente.status == 0:
        return "El precio actual no está disponible"
    
    tipo_productos = get_all_available_tipo_producto()
    if request.method == 'POST':
        tipo = request.form.get('tipo_producto')
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
            # y esta oculto (o no), lo eliminamos y el nuevo
            # tomará su lugar
            if copy :
                remove_precio(copy)
            precio_existente.id_tipo = tipo
            precio_existente.precio = precio
            add_precio(precio_existente)
            flash('Precio actualizado con éxito a', precio_existente.producto.nombre)
            return redirect(url_for('precios.main'))
        else:
            flash(error)


    return render_template('cafeteria/crud/update_precio.html', precio = precio_existente, tipo_productos = tipo_productos)

#DELETE PRECIO
@precios.route('/eliminar-precio/<int:id_producto>%<int:id_tipo_producto>')
@requiere_inicio_sesion
@admin
def delete_precio(id_producto, id_tipo_producto):
    '''Soft delete precio'''
    precio = get_precio_unico(id_producto, id_tipo_producto)
    hide_precio(precio)
    return redirect(url_for('productos.main'))
    