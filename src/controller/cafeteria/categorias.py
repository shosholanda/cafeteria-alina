from flask import (
    render_template, Blueprint, flash, g, redirect, request, session, url_for
)

from werkzeug.exceptions import abort

from src.model.categoria import Categoria
from src.model.repository.repo_categoria import *

from src.controller.auth import requiere_inicio_sesion, admin

''' Controlador para las operaciones de producto '''

categorias = Blueprint('categorias', __name__, url_prefix='/categorias') # Crear la sesion


# GET
@categorias.route('/')
@requiere_inicio_sesion
@admin
def main():
    return redirect(url_for('categorias.create_categoria'))

# CREATE
@categorias.route('/nueva-categoria', methods=['GET', 'POST'])
@requiere_inicio_sesion
@admin
def create_categoria():
    categorias = get_all_categorias()
    error = None
    if request.method == 'POST':
        categoria_name = request.form.get('categoria')
        descripcion = request.form.get('descripcion')

        if categoria_name:
            categoria_name = categoria_name.strip().title()
        if descripcion:
            descripcion = descripcion.strip().replace('\n', ' ')
        else:
            descripcion = 'Sin descripcion'

        if not get_categoria_by_name(categoria_name):
            nueva_categoria = Categoria(categoria_name, descripcion)
            add_categoria(nueva_categoria)
            # Actualizar página
            flash('Categoría agregada con éxito!')
            return redirect(url_for('categorias.create_categoria'))

        else:
            error = 'La categoria ya existe'
        if error:
            flash(error)

    return render_template('cafeteria/crud/create_categoria.html', categorias = categorias)

# UPDATE
@categorias.route('/editar-categoria/<int:id_categoria>', methods=['GET', 'POST'])
@requiere_inicio_sesion
@admin
def update_categoria(id_categoria):
    categoria_a_modificar = get_categoria_by_id(id_categoria)

    if not categoria_a_modificar:
        abort(404)

    error = None
    if request.method == 'POST':
        categoria_name = request.form.get('categoria')
        descripcion = request.form.get('descripcion')

        if categoria_name:
            categoria_name = categoria_name.strip().title()
        if descripcion:
            descripcion = descripcion.strip().replace('\n', ' ')
        else:
            descripcion = 'Sin descripcion'

        copy = get_categoria_by_name(categoria_name)
        if not copy or copy.id == categoria_a_modificar.id:
            categoria_a_modificar.nombre = categoria_name
            categoria_a_modificar.descripcion = descripcion
            add_categoria(categoria_a_modificar)
            flash('Categoria actualizada correctamente!')
            return redirect(url_for('categorias.create_categoria'))
        else:
            error = 'La categoria ya existe'
        if error:
            flash(error)

    return render_template('cafeteria/crud/update_categoria.html', categoria = categoria_a_modificar, categorias = get_all_categorias())

# DELETE
@categorias.route('/eliminar-categoria/<int:id_categoria>', methods=['GET', 'POST'])
@requiere_inicio_sesion
@admin
def delete_categoria():
    # AAA ?
    return "No se pueden eliminar categorias!"