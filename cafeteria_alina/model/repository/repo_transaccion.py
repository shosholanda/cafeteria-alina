import datetime

# Importamos las tablas
from cafeteria_alina.model.precio import Precio
from cafeteria_alina.model.producto import Producto
from cafeteria_alina.model.tipo_producto import TipoProducto
from cafeteria_alina.model.venta import Venta
from cafeteria_alina.model.transaccion import Transaccion

from sqlalchemy import func

#Importar la base de datos.
from cafeteria_alina import db

def get_all_transactions():
    '''Obtiene todas las transacciones'''
    return Transaccion.query.all()

def get_daily_transactions(day):
    '''Obtiene las transacciones hechas en un día'''
    today = day
    tomorrow = today.replace(day=today.day+1).strftime('%Y-%m-%d %H:%M:%S')
    today = today.strftime('%Y-%m-%d %H:%M:%S')
    return get_transactions_by_date(today, tomorrow)

def get_transactions_by_date(init, finish):
    '''Regresa todas las ventas hechas entre init y finish
    Combina las tablas para tener la consulta más completa
    SELECT * FROM venta 
        INNER JOIN transaccion ON transaccion.referencia = venta.referencia 
        INNER JOIN tipo_producto ON transaccion.tipo = tipo_producto.id 
        INNER JOIN producto ON producto.id = transaccion.id_producto 
        WHERE fecha < '2024-06-24';
    '''
    return Venta.query\
        .join(Transaccion, Venta.referencia == Transaccion.id_referencia)\
        .join(Precio, Transaccion.id_precio == Precio.id)\
        .filter(Venta.fecha.between(init, finish)).order_by(-Venta.referencia)


def add_transaction(transaction):
    '''Añade esta transaccion a la base de datos. Si existe lo reemplaza?
    La transaccion debe tener todos sus atributos ya definidos.'''
    db.session.add(transaction) #Añadir
    db.session.commit()     #Guardar y actualizar


### Ventas
def get_total_ventas():
    '''Suma total de todas las ventas'''
    return db.session.query(func.sum(Venta.total)).scalar()

def get_daily_total_ventas(day):
    '''Obtiene el total de ventas hechas en un día'''
    today = day
    tomorrow = today.replace(day=today.day+1).strftime('%Y-%m-%d %H:%M:%S')
    today = today.strftime('%Y-%m-%d %H:%M:%S')
    return get_total_ventas_by_date(today, tomorrow)

def get_total_ventas_by_date(init, finish):
    '''Obtienew el total de las ventas hechas en el rango de fecha
    db = query
    SELECT SUM(total) FROM QUERY
        WHERE fecha < finish ;'''
    return db.session.query(func.sum(Transaccion.subtotal))\
        .join(Venta, Venta.referencia == Transaccion.id_referencia)\
        .filter(Venta.fecha.between(init, finish)).scalar()

def get_last_ref():
    '''Obtiene el número de la última referencia'''
    return db.session.query(func.max(Venta.referencia)).scalar()

