from flask import (
    render_template, Blueprint, flash, g, redirect, request, session, url_for
)

from werkzeug.exceptions import abort

from cafeteria_alina.model.repository.repo_gasto import *
from cafeteria_alina.model.repository.repo_sucursal import get_all_sucursales
from cafeteria_alina.model.repository.repo_tipo_gasto import *

from cafeteria_alina.controller.auth import requiere_inicio_sesion, admin


''' Controlador para las operaciones de gasto '''

gastos = Blueprint('gastos', __name__, url_prefix='/gastos') # Crear la sesion

# Página de gastos de página. Debes ser admin
@gastos.route('/')
@requiere_inicio_sesion
@admin
def main():
    gastos = get_all_weekly_gastos()
    total = get_all_weekly_total_gastos()
    return render_template('cafeteria/gastos.html', gastos = gastos, total = total)


# CREATE PRECIO
@gastos.route('/agregar-gasto/', methods=('GET', 'POST'))
@requiere_inicio_sesion
@admin
def create_gasto():
    '''Crea un nuevo gasto para el gastorepo_gastos <id>'''
    if request.method == 'POST':
        # AAA Ponerlo automáticamente
        id_sucursal = request.form.get('sucursal')
        nombre = request.form.get('nombre')
        tipo_gasto = request.form.get('tipo_gasto')
        monto = request.form.get('cantidad')

        error = None

        try:
            id_sucursal = int(id_sucursal)
            tipo_gasto = int(tipo_gasto)
            monto = float(monto)
        except ValueError:
            error = 'No se pudo convertir la información correctamente'

        if not error:
            gasto = Gasto(id_sucursal=id_sucursal,
                          id_tipo_gasto= tipo_gasto,
                          nombre = nombre,
                          cantidad= monto)
            add_gasto(gasto)
            flash('Nuevo gasto agregado correctamente!')
            return redirect(url_for('gastos.main'))

   
    return render_template('cafeteria/crud/create_gasto.html',
                            tipo_gastos = get_all_available_tipo_gasto(),
                            sucursales = get_all_sucursales())

#UPDATE PRECIO
@gastos.route('/editar-gasto/<id>', methods=('GET', 'POST'))
@requiere_inicio_sesion
@admin
def update_gasto(id):
    gasto = get_gasto_by_id(id)
    tipos = get_all_tipo_gasto()
    sucursales = get_all_sucursales()

    if request.method == 'POST':
        # AAA Ponerlo automáticamente
        id_sucursal = request.form.get('sucursal')
        nombre = request.form.get('nombre')
        tipo_gasto = request.form.get('tipo_gasto')
        monto = request.form.get('cantidad')

        error = None

        try:
            id_sucursal = int(id_sucursal)
            tipo_gasto = int(tipo_gasto)
            monto = float(monto)
        except ValueError:
            error = 'No se pudo convertir la información correctamente'

        if not error:
            gasto.id_sucursal = id_sucursal
            gasto.nombre = nombre
            gasto.id_tipo_gasto = tipo_gasto
            gasto.cantidad = monto
            add_gasto(gasto)
            flash('Gasto actualizado correctamente!')
            return redirect(url_for('gastos.main'))
    

    return render_template('cafeteria/crud/update_gasto.html', gasto = gasto, tipo_gastos = tipos, sucursales = sucursales)


#DELETE PRECIO
@gastos.route('/eliminar-gasto/<int:id>')
@requiere_inicio_sesion
@admin
def delete_gasto(id):
    '''Soft delete gasto'''
    gasto = get_gasto_by_id(id)
    hide_gasto(gasto)
    return redirect(url_for('gastos.main'))
    