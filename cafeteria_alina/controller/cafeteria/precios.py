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
        tam = request.form.get('tipo')
        
        error = None
        try:
            precio = float(request.form.get('precio'))
            nuevo_precio = get_precio_unico(id, tam)
            if nuevo_precio:
                error = 'Ya existe esta asignación'
        except ValueError:
            error = 'No se ha ingresado un precio válido. Ej. 14.22'
        

        if error:
            flash(error)
        else:
            precio = Precio(id, tam, precio)
            agregar_precio(precio)
            return render_template('cafeteria/success.html', tipo = 'Producto', crud = 'agregado', obj = precio)
        
    return render_template('cafeteria/crud/create_precio.html', producto = producto, precios = precios)

#UPDATE PRECIO
@precios.route('/editar-precio/<id>_<tipo>', methods=('GET', 'POST'))
@requiere_inicio_sesion
def update_precio(id, tipo):
    precio_existente = get_precio_unico(id, tipo)
    if request.method == 'POST':
        tipo = request.form.get('tamaño')
        
        error = None
        try:
            precio = float(request.form.get('precio'))
        except ValueError:
            error = 'No se ha ingresado un precio válido. Ej. 14.22'
        if precio_existente:
            precio_existente.precio = precio
            agregar_precio(precio_existente)
        else:
            agregar_precio(Precio(id, tipo, precio))
        
        if error:
            flash(error)
        else:
            return "Precio actualizado correctamente a " + id


    return render_template('cafeteria/crud/update_precio.html', precio = precio_existente)

#DELETE PRECIO
@precios.route('/eliminar-precio/<id>_<tipo>')
@requiere_inicio_sesion
def delete_precio(id, tipo):
    precio = get_precio_unico(id, tipo)
    eliminar_precio(precio)
    return redirect(url_for('precio.precios_por_producto', id = id))
    