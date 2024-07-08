from flask import (
    jsonify, render_template, Blueprint, flash, g, redirect, request, session, url_for
)

from src.model.repository.repo_precio import *
from src.model.repository.repo_producto import *
from src.model.repository.repo_categoria import *
from src.model.repository.repo_tipo_producto import *
from src.model.repository.repo_transaccion import *
from src.model.repository.repo_usuario import *
from src.model.transaccion import Transaccion
from src.model.venta import Venta

from src.controller.auth import requiere_inicio_sesion, admin

''' Controlador para las operaciones de producto '''

ventas = Blueprint('ventas', __name__,url_prefix='/ventas') # Crear la sesion

# Ventana de ventas
@ventas.route('/')
@requiere_inicio_sesion
# Trabajador
@admin
def main():
    today = datetime.datetime.now()
    ventas_del_dia = get_daily_transactions(today)
    total_del_dia = get_daily_total_ventas(today)
    return render_template('cafeteria/ventas.html', ventas = ventas_del_dia, total = total_del_dia)

# Crear una venta (confirmar)
@ventas.route('/nueva-venta', methods=['GET', 'POST'])
@requiere_inicio_sesion
#Trabajador
@admin
def create_venta():
    productos = get_ordered_productos_by_name()
    tipos = get_all_available_tipo_producto()
    user = get_full_usuario(g.user.correo)

    if not user.id_sucursal:
        return 'No puedes crear ventas si no estas asociado a una sucursal!'

    if request.method == 'POST':
        #Para postman sí es necesario
        body = request.json#['body']
        cart = body['cart']
        total = body['total']
        error = None

        v = Venta(total, user.correo, user.id_sucursal)
        add_transaction(v)
        last_ref = get_last_ref()

        for item in cart:
            try:
                # Get precio from query + categoria
                precio = float(item['precio'])
                cant = int(item['cantidad'])
                subtot = float(item['subtotal'])
            except ValueError:
                error = "No se pudo recibir la información correctamente"
                break

            t = Transaccion(last_ref, precio, cant, subtot)
            add_transaction(t)
        
        if not error:
            flash('Venta hecha con éxito!')
            return redirect(url_for('ventas.main'))
            # return jsonify({"redirect": url_for('ventas.main')}), 200
        flash(error)
        
    return render_template('cafeteria/crud/create_venta.html', productos = productos, tipos = tipos)

#QUERY para cambiar de id_tipo_producto
@ventas.route('/get-tipos-por-producto/<int:id_producto>')
@requiere_inicio_sesion
#Trabajador
@admin
def get_tipos_por_producto(id_producto):
    tipos = get_tipos_por_producto_available(id_producto)
    # Convertir a JSON la consulta
    tipos_json = [{'id_tipo_producto': tipo.id_tipo_producto,
                   'tipo_producto':tipo.tipo_producto.nombre} for tipo in tipos]
    return jsonify(tipos_json)

#QUERY para obtener el precio de un producto
@ventas.route('/get-precio/<int:id_producto>&<int:id_tipo_producto>')
@requiere_inicio_sesion
#Trabajador
@admin
def get_precio(id_producto, id_tipo_producto):
    precio = get_precio_unico(id_producto, id_tipo_producto)
    # Convertir a JSON la consulta
    tipos_json = {'id': precio.id,
                  'precio': precio.precio}
    return jsonify(tipos_json)
