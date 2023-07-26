from flask import (
    render_template, Blueprint, flash, g, redirect, request, session, url_for
)

from werkzeug.exceptions import abort

# Create the following databases
from cafeteria_alina.model.producto import Producto
from cafeteria_alina.model.tamaño import Tamaño

from cafeteria_alina.model.repository.repo_producto import *

from cafeteria_alina.controller.auth import requiere_inicio_sesion

from cafeteria_alina import db


''' Controlador para las operaciones de producto '''

productos = Blueprint('productos', __name__, url_prefix='/productos') # Crear la sesion

# Página de productos de página. EStá afuera de la sesion
@productos.route('/')
@requiere_inicio_sesion
def main():
    return render_template('cafeteria/productos.html')


# CREATE PRODUCTO
@productos.route('/agregar-producto', methods=('GET', 'POST'))
@requiere_inicio_sesion
def create_producto():
    if request.method == 'POST':

        nombre = request.form.get('nombre')
        tamaño = request.form.get('tamaño')
        precio = request.form.get('precio')

        id_producto = nombre.strip().lower().replace(' ', '_') + f'_{tamaño}'



        producto = get_producto_id(id_producto)
        error = None

        if producto:
            error = f'El producto {id_producto} ya existe. Indique otro producto'
        else:
            try:
                precio = float(precio)
                producto = Producto(id_producto, nombre, tamaño, precio)
            except ValueError:
                error = 'El precio no es válido. Ejemplo: 14.5'

        if not error:
            return "Producto registrado exitosamente!"
        else:
            flash(error)
    return render_template('cafeteria/crud/create_producto.html')
