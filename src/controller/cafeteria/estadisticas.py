import datetime
from flask import (
    Response, render_template, Blueprint, flash, g, redirect, request, session, url_for
)

from werkzeug.exceptions import abort

from src.model.repository.repo_gasto import *
from src.model.repository.repo_transaccion import *

from src.controller.auth import requiere_inicio_sesion, admin

''' Controlador para las operaciones de producto '''

estadisticas = Blueprint('estadisticas', __name__, url_prefix='/estadisticas') # Crear la sesion

# Ventana de estadísticas
@estadisticas.route('/', methods=['GET', 'POST'])
@requiere_inicio_sesion
@admin
def main():
    finish = datetime.datetime.now()
    init = finish - datetime.timedelta(days=30)
    return redirect(url_for('estadisticas.change_date', init = init, finish = finish))

@estadisticas.route('/change/<init>&<finish>', methods=('POST', 'GET'))
@requiere_inicio_sesion
@admin
def change_date(init, finish):
    if finish <= init:
        flash('El inicio SIEMPRE debe ser antes que el final')
        return redirect(url_for('estadisticas.main'))

    if request.method == 'POST':
        init = request.form.get('init')
        finish = request.form.get('finish')
        if not init or not finish:
            flash('Se deben de poner bien las fechas!')
            return redirect(url_for('estadisticas.main'))
        return redirect(url_for('estadisticas.change_date', init = init, finish = finish))

    # Todos son listas, o 0 if None
    top_productos = get_top_productos(10)
    ganancias = get_total_ventas_by_date(init, finish)
    perdidas = get_total_gastos_by_date(init, finish)
    
    historial, total = get_ventas_and_gastos_by_date(init, finish)
    
    return render_template('cafeteria/estadisticas.html',
                           init = init,
                           finish = finish,
                           ganancias = ganancias if ganancias != None else 0,
                           perdidas = perdidas if perdidas != None else 0,
                           top_productos = top_productos,
                           historial = historial,
                           total = total)
