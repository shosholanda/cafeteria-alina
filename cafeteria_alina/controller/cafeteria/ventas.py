from flask import (
    jsonify, render_template, Blueprint, flash, g, redirect, request, session, url_for
)


from cafeteria_alina.model.repository.repo_precio import *
from cafeteria_alina.model.repository.repo_producto import *
from cafeteria_alina.model.repository.repo_tipo_producto import *
from cafeteria_alina.model.repository.repo_transaccion import *
from cafeteria_alina.model.transaccion import Transaccion
from cafeteria_alina.model.venta import Venta

from cafeteria_alina.controller.auth import requiere_inicio_sesion, admin

''' Controlador para las operaciones de producto '''

ventas = Blueprint('ventas', __name__,url_prefix='/ventas') # Crear la sesion

# Ventana de ventas
@ventas.route('/')
@requiere_inicio_sesion
# Trabajador
@admin
def main():
    today = datetime.date.today()
    ventas_del_dia = get_daily_transactions(today)
    total_del_dia = get_daily_total_ventas(today)
    return render_template('cafeteria/ventas.html', ventas = ventas_del_dia, total = total_del_dia)

# Crear una venta (confirmar)
@ventas.route('/nueva-venta', methods=['GET', 'POST'])
@requiere_inicio_sesion
#Trabajador
@admin
def create_venta():
    productos = get_all_available_productos()
    tipos = get_all_available_tipo_producto()
    if request.method == 'POST':
        #From postman sí es necesario
        body = request.json#['body']
        cart = body['cart']
        total = body['total']
        
        error = None
        v = Venta(total, session['usuario'])
        add_transaction(v)
        last_ref = get_last_ref()

        for item in cart:
            try:
                id_prod = int(item['producto'])
                tipo = int(item['tipo'])
                precio = float(item['precio'])
                cant = int(item['cantidad'])
                subtot = float(item['subtotal'])
            except ValueError:
                error = "No se pudo recibir la información correctamente"
                break

            t = Transaccion(last_ref, id_prod, tipo, precio, cant, subtot)
            add_transaction(t)
        
        if not error:
            return redirect(url_for('ventas.main'))
            # return jsonify({"redirect": url_for('ventas.main')}), 200
        flash(error)
        
    return render_template('cafeteria/crud/create_venta.html', productos = productos, tipos = tipos)

#QUERY
@ventas.route('/tipos-por-producto/<int:id_producto>')
@requiere_inicio_sesion
#Trabajador
@admin
def tipos_por_producto(id_producto):
    tipos = get_tipos_por_producto_available(id_producto)
    # Convertir a JSON la consulta
    tipos_json = [{'id_producto': id_producto,
                   'id_tipo': tipo.id_tipo,
                   'tipo':tipo.tipo.tipo, 
                   'precio':tipo.precio} for tipo in tipos]
    return jsonify(tipos_json)