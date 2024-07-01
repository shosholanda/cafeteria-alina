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
    sucursales = get_all_available_sucursales()
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

        if not get_sucursal_by_nombre(nombre):
            sucursal = Sucursal(nombre=nombre,
                                calle=calle,
                                numero=número,
                                colonia=colonia,
                                municipio=municipio,
                                ciudad=ciudad,
                                pais=pais,
                                fecha_inaguracion=fecha)
            add_sucursal(sucursal)
            flash('Sucursal añadida con éxito!')
            return redirect(url_for('sucursales.main'))
        else:
            flash('No se pueden registrar 2 sucursales en el mismo lugar!')
    return render_template('cafeteria/crud/create_sucursal.html')

#UPDATE PRODUCTO
@sucursales.route('/editar-sucursal/<int:id>', methods=('GET', 'POST'))
@requiere_inicio_sesion
@admin
def update_sucursal(id):
    sucursal = get_sucursal_by_id(id)

    error = None
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        calle = request.form.get('calle')
        número = request.form.get('número')
        colonia = request.form.get('colonia')
        municipio = request.form.get('municipio')
        ciudad = request.form.get('ciudad')
        pais = request.form.get('pais')
        fecha = request.form.get('fecha')

        # AAA Validar más a detalle
        copy = get_sucursal_by_nombre(nombre)
        if not copy or copy.id == id:
            sucursal.nombre = nombre
            sucursal.calle = calle
            sucursal.numero = número
            sucursal.colonia = colonia
            sucursal.municipio = municipio
            sucursal.ciudad = ciudad
            sucursal.pais = pais
            sucursal.fecha = fecha

            add_sucursal(sucursal)
            flash('Sucursal modificada con éxito!')
            return redirect(url_for('sucursales.main'))
        else:
            flash('No se pueden registrar 2 con el mismo nombre!')

    return render_template('cafeteria/crud/update_sucursal.html', sucursal = sucursal)

#DELETE PRODUCTO
@sucursales.route('/eliminar-sucursal/<int:id>')
@requiere_inicio_sesion
@admin
def delete_sucursal(id):
    '''Nunca borramos ningun sucursal'''
    sucursal = get_sucursal_by_id(id)
    hide_sucursal(sucursal)
    return redirect(url_for('sucursales.main'))


