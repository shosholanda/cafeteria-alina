from flask import (
    render_template, Blueprint, flash, g, redirect, request, session, url_for
)

from werkzeug.exceptions import abort

from src.model.repository.repo_tipo_gasto import *

from src.controller.auth import requiere_inicio_sesion, admin


''' Controlador para las operaciones de gasto '''

tipo_gastos = Blueprint('tipo-gastos', __name__, url_prefix='/tipo-gastos') # Crear la sesion

# Página de tipo_gastos de página. EStá afuera de la sesion
@tipo_gastos.route('/')
@requiere_inicio_sesion
@admin
def main():
    tipo_gastos = get_all_tipo_gasto()
    return render_template('cafeteria/crud/create_tipo_gasto.html', tipo_gastos = tipo_gastos)


# CREATE PRODUCTO
@tipo_gastos.route('/agregar-tipo', methods=('GET', 'POST'))
@requiere_inicio_sesion
@admin
def create_tipo():
    if request.method == 'POST':
        nombre = request.form.get('nombre').strip().title()
        descripcion = request.form.get('descripcion').strip().replace('\n', ' ')

        error = ''

        copy = get_tipo_gasto_by_name(nombre)
        if not copy:
            nuevo_gasto = TipoGasto(nombre, descripcion)
            add_tipo_gasto(nuevo_gasto)

        elif copy.status == 0:
            copy.status = 1
            add_tipo_gasto(copy)
        else:
            error = 'Ya existe ese tipo de pago'

        if not error:
            flash('Tipo de gasto añadido correctamente!')
            return redirect(url_for('tipo-gastos.create_tipo'))
        
        flash(error)
    return render_template('cafeteria/crud/create_tipo_gasto.html', tipo_gastos = get_all_tipo_gasto())

#UPDATE PRODUCTO
@tipo_gastos.route('/editar/<int:id_tipo_gasto>', methods=('GET', 'POST'))
@requiere_inicio_sesion
@admin
def update_tipo_gasto(id_tipo_gasto):
    gasto = get_tipo_gasto_by_id(id_tipo_gasto)
    if not gasto:
        abort(404)

    if request.method == 'POST':
        nombre = request.form.get('nombre')
        descripcion = request.form.get('descripcion')
        status = request.form.get('status') 

        status = True if status != None else 0

        error = None
        if not nombre:
            error = 'Se requiere de al menos un nombre'
        else:
            gasto.nombre = nombre
            if not descripcion or descripcion.strip() == '':
                gasto.descripcion = "Sin descripcion"
            gasto.descripcion = descripcion
            gasto.status = status
            add_tipo_gasto(gasto)
            flash('Se actualizó correctamente el tipo de gasto!')
            return redirect(url_for('tipo-gastos.update_tipo_gasto', id_tipo_gasto = id_tipo_gasto))
        
        flash(error)

    return render_template('cafeteria/crud/update_tipo_gasto.html', gasto = gasto, tipo_gastos = get_all_tipo_gasto())

#DELETE PRODUCTO
@tipo_gastos.route('/eliminar/<int:id_tipo_gasto>')
@requiere_inicio_sesion
@admin
def delete_tipo_gasto(id_tipo_gasto):
    gasto = get_tipo_gasto_by_id(id_tipo_gasto)
    if not gasto:
        abort(404)
    hide_tipo_gasto(gasto)
    return redirect(url_for('tipo-gastos.create_tipo'))
