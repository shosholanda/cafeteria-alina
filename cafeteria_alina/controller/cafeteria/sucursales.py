from flask import (
    render_template, Blueprint, flash, g, redirect, request, session, url_for
)

from werkzeug.exceptions import abort

# Create the following databases
from cafeteria_alina.model.sucursal import Sucursal

from cafeteria_alina.model.repository.repo_sucursal import *

from cafeteria_alina.controller.auth import requiere_inicio_sesion, admin


''' Controlador para las operaciones de sucursal '''

sucursales = Blueprint('sucursales', __name__, url_prefix='/sucursales') # Crear la sesion

# Página de sucursales de página. EStá afuera de la sesion
@sucursales.route('/')
@requiere_inicio_sesion
@admin
def main():
    sucursales = get_all_sucursales()
    return render_template('cafeteria/sucursales.html', sucursales = sucursales)


# CREATE PRODUCTO
@sucursales.route('/agregar-sucursal', methods=('GET', 'POST'))
@requiere_inicio_sesion
@admin
def create_sucursal():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        calle = request.form.get('calle')
        número = request.form.get('número')
        colonia = request.form.get('colonia')
        municipio = request.form.get('municipio')
        ciudad = request.form.get('ciudad')
        pais = request.form.get('pais')
        fecha = request.form.get('fecha')

        sucursal = Sucursal(nombre=nombre,
                            calle=calle,
                            numero=número,
                            colonia=colonia,
                            municipio=municipio,
                            ciudad=ciudad,
                            pais=pais,
                            inaguracion=fecha)
        add_sucursal(sucursal)
        return render_template('cafeteria/success.html', tipo = 'Sucursal', crud = 'agregada')
    
    return render_template('cafeteria/crud/create_sucursal.html')

#UPDATE PRODUCTO
@sucursales.route('/editar-sucursal/<int:id>', methods=('GET', 'POST'))
@requiere_inicio_sesion
@admin
def update_sucursal(id):
    sucursal = get_sucursal_by_id(id)

    error = None
    if request.method == 'POST':

        if error:
            flash(error)
        else:
            return render_template('cafeteria/success.html', tipo = 'Producto', crud = 'modificado')

    return render_template('cafeteria/crud/update_sucursal.html', sucursal = sucursal, categorias = categorias)

#DELETE PRODUCTO
@sucursales.route('/eliminar-sucursal/<int:id>')
@requiere_inicio_sesion
@admin
def delete_sucursal(id):
    '''Nunca borramos ningun sucursal'''
    sucursal = get_sucursal_by_id(id)
    hide_sucursal(sucursal)
    return redirect(url_for('sucursales.main'))


