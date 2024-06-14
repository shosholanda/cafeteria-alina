from flask import (
    render_template, Blueprint, flash, g, redirect, request, session, url_for
)

from werkzeug.exceptions import abort

from cafeteria_alina.model.repository.repo_producto import *

from cafeteria_alina.controller.auth import requiere_inicio_sesion


''' Controlador para las operaciones de precio '''

precio = Blueprint('precio', __name__, url_prefix='/precio') # Crear la sesion

# Página de precio de página. EStá afuera de la sesion
@precio.route('/')
@requiere_inicio_sesion
def main():
    # precios =read_precios()
    # return render_template('cafeteria/precio.html', precios = precios)
    return "Aquí mostramos la lista de productos"


# CREATE PRECIO
@precio.route('/agregar-precio/<id_prod>', methods=('GET', 'POST'))
@requiere_inicio_sesion
def create_precio(id_prod):
    # producto = get_producto_id(id_prod)
    # precios = read_precios(id_prod)
    # if request.method == 'POST':
    #     tam = request.form.get('tamaño')
        
    #     error = None
    #     try:
    #         precio = float(request.form.get('precio'))
    #     except ValueError:
    #         error = 'No se ha ingresado un precio válido. Ej. 14.22'

    #     if error:
    #         flash(error)
    #     else:
    #         precio = Precio(id_prod, tam, precio)
    #         agregar_precio(precio)
    #         return render_template('cafeteria/success.html', tipo = 'Precio', crud = 'agregado', obj = precio)
        
    # return render_template('cafeteria/crud/create_precio.html', producto = producto, precios = precios)
    return "Aquí agregamos "

#UPDATE PRECIO
@precio.route('/editar-precio/<id_prod>_<tam>', methods=('GET', 'POST'))
@requiere_inicio_sesion
def update_precio(id_prod, tam):
    precio_existente = get_precio_unico(id_prod, tam)
    if request.method == 'POST':
        tam = request.form.get('tamaño')
        
        error = None
        try:
            precio = float(request.form.get('precio'))
        except ValueError:
            error = 'No se ha ingresado un precio válido. Ej. 14.22'
        if precio_existente:
            precio_existente.precio = precio
            agregar_precio(precio_existente)
        else:
            agregar_precio(Precio(id_prod, tam, precio))
        
        if error:
            flash(error)
        else:
            return "Precio actualizado correctamente a " + id_prod


    return render_template('cafeteria/crud/update_precio.html', precio = precio_existente)

#DELETE PRECIO
@precio.route('/eliminar-precio/<id_prod>_<tam>')
@requiere_inicio_sesion
def delete_precio(id_prod, tam):
    precio = get_precio_unico(id_prod, tam)
    eliminar_precio(precio)
    return redirect(url_for('precio.precios_por_producto', id_prod = id_prod))

#READ PRECIO
@precio.route('/<id_prod>', methods=('GET', 'POST'))
@requiere_inicio_sesion
def precios_por_producto(id_prod):
    '''Mostrar todos los subprecio de cierto precio. Los subprecio 
    son las variaciones de precios de un precio, dependiendo del tamaño''' 
    producto = get_producto_id(id_prod)
    precios = read_precios(id_prod)
    return render_template('cafeteria/precios.html', precios = precios, producto = producto)
    