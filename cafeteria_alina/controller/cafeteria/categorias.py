from flask import (
    render_template, Blueprint, flash, g, redirect, request, session, url_for
)

from werkzeug.exceptions import abort

from cafeteria_alina.model.categoria import Categoria
from cafeteria_alina.model.repository.repo_categoria import *

from cafeteria_alina.controller.auth import requiere_inicio_sesion, admin


''' Controlador para las operaciones de producto '''

categorias = Blueprint('categorias', __name__, url_prefix='/categorias') # Crear la sesion


# Ventana de estadísticas
@categorias.route('/')
@requiere_inicio_sesion
def main():
    return "categorias"

# Ventana de estadísticas
@categorias.route('/nueva-categoria', methods=['GET', 'POST'])
@requiere_inicio_sesion
@admin
def create_categoria():
    categorias = get_all_categorias()
    print(categorias)
    error = None
    if request.method == 'POST':
        categoria_name = request.form.get('categoria')
        descripcion = request.form.get('descripcion')

        if categoria_name:
            categoria_name = categoria_name.strip().title()
        if descripcion:
            descripcion = descripcion.strip().replace('\n', ' ')

        if not get_categoria_by_name(categoria_name):
            nueva_categoria = Categoria(categoria_name, descripcion)
            add_categoria(nueva_categoria)
            return render_template('cafeteria/success.html', tipo = 'Categoria', crud = 'agregada')

        else:
            error = 'La categoria ya existe'
        
        flash(error)

    return render_template('cafeteria/crud/create_categoria.html', categorias = categorias)