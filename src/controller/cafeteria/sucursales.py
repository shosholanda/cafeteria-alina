from flask import (
    render_template, Blueprint, flash, g, redirect, request, session, url_for
)

from werkzeug.exceptions import abort

from src.model.sucursal import Sucursal

from src.model.repository.repo_sucursal import *

from src.controller.auth import requiere_inicio_sesion, admin


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
        nombre = request.form.get('nombre').strip().upper()
        calle = request.form.get('calle').strip().title()
        numero = request.form.get('numero').strip().title()
        colonia = request.form.get('colonia').strip().title()
        municipio = request.form.get('municipio').strip().title()
        ciudad = request.form.get('ciudad').strip().title()
        pais = request.form.get('pais').strip().title()
        fecha = request.form.get('fecha')

        if not get_sucursal_by_nombre(nombre):
            sucursal = Sucursal(nombre=nombre,
                                calle=calle,
                                numero=numero,
                                colonia=colonia,
                                municipio=municipio,
                                ciudad=ciudad,
                                pais=pais,
                                fecha_inaguracion=fecha)
            add_sucursal(sucursal)
            flash('Sucursal añadida con éxito!')
            return redirect(url_for('sucursales.main'))
        else:
            flash('No se pueden registrar 2 sucursales con el mismo nombre!')
    return render_template('cafeteria/crud/create_sucursal.html')

#UPDATE PRODUCTO
@sucursales.route('/editar-sucursal/<int:id_sucursal>', methods=('GET', 'POST'))
@requiere_inicio_sesion
@admin
def update_sucursal(id_sucursal):
    sucursal = get_sucursal_by_id(id_sucursal)

    error = None
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        calle = request.form.get('calle')
        numero = request.form.get('numero')
        colonia = request.form.get('colonia')
        municipio = request.form.get('municipio')
        ciudad = request.form.get('ciudad')
        pais = request.form.get('pais')
        fecha = request.form.get('fecha')

        # AAA Validar más a detalle
        copy = get_sucursal_by_nombre(nombre)
        if not copy or copy.id == id_sucursal:
            sucursal.nombre = nombre
            sucursal.calle = calle
            sucursal.numero = numero
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
@sucursales.route('/eliminar-sucursal/<int:id_sucursal>')
@requiere_inicio_sesion
@admin
def delete_sucursal(id_sucursal):
    '''Nunca borramos ningun sucursal'''
    sucursal = get_sucursal_by_id(id_sucursal)
    if not sucursal:
        abort(404)
    hide_sucursal(sucursal)
    return redirect(url_for('sucursales.main'))


