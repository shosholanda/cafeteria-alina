import datetime
from flask import (
    render_template, Blueprint, flash, g, redirect, request, session, url_for
)

from werkzeug.exceptions import abort

from cafeteria_alina.model.repository.repo_gasto import *
from cafeteria_alina.model.repository.repo_transaccion import *

from cafeteria_alina.controller.auth import requiere_inicio_sesion, admin

from cafeteria_alina import db


''' Controlador para las operaciones de producto '''

estadisticas = Blueprint('estadisticas', __name__, url_prefix='/estadisticas') # Crear la sesion


# Ventana de estadísticas
@estadisticas.route('/', methods=['GET', 'POST'])
@requiere_inicio_sesion
@admin
def main():
    finish = datetime.date.today()
    init = finish - datetime.timedelta(days=30)
    print(init, finish)

    return redirect(url_for('estadisticas.change_date', init = init, finish = finish))

@estadisticas.route('/change/<init>&<finish>', methods=('POST', 'GET'))
@requiere_inicio_sesion
@admin
def change_date(init, finish):
    if request.method == 'POST':
        init = request.form.get('init')
        finish = request.form.get('finish')
        return redirect(url_for('estadisticas.change_date', init = init, finish = finish))

    top_productos = get_top_productos(10)
    ganancias = get_total_ventas_by_date(init, finish)
    perdidas = get_total_gastos_by_date(init, finish)

    historial, total = get_ventas_and_gastos_by_date(init, finish)
    
    return render_template('cafeteria/estadisticas.html',
                           init = init,
                           finish = finish,
                           ganancias = ganancias,
                           perdidas = perdidas,
                           top_productos = top_productos,
                           historial = historial,
                           total = total)