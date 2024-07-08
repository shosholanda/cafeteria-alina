import datetime

# Importamos las tablas
from src.model.categoria import Categoria
from src.model.precio import Precio
from src.model.producto import Producto
from src.model.tipo_producto import TipoProducto
from src.model.venta import Venta
from src.model.transaccion import Transaccion

from src.model.repository.repo_gasto import *

from sqlalchemy import desc, func, literal

#Importar la base de datos.
from src import db

def get_all_transactions():
    '''Obtiene todas las transacciones'''
    return Transaccion.query.all()

def get_daily_transactions(today):
    '''Obtiene las transacciones hechas en un día'''
    tomorrow = today + datetime.timedelta(days=1)
    tomorrow = tomorrow.replace(hour=23, minute=59, second=59)
    today = today.replace(hour=0, minute=0, second=0)
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

def get_top_productos(top):
    '''Obtiene el top de productos ventidos de esta sucursal'''
    prod = db.session.query(
                func.sum(
                    Transaccion.cantidad).label('cantidad_total'), #La primera es la que se suma
                    # Las demás son select *
                    Producto.nombre.label('producto'),
                    TipoProducto.nombre.label('tipo_producto'),
                    Categoria.nombre.label('categoria'),
                    Precio.precio,
                )\
            .group_by(Transaccion.id_precio)\
            .order_by(desc('cantidad_total'))\
            .join(Precio, Transaccion.id_precio == Precio.id)\
            .join(Producto, Precio.id_producto == Producto.id)\
            .join(TipoProducto, Precio.id_tipo_producto == TipoProducto.id)\
            .join(Categoria, Producto.id_categoria == Categoria.id)\
            .limit(top)
    # Perra madre otra vez los JSON
    productos = [{
                    'cantidad':p[0],
                    'producto':p[1],
                    'tipo':p[2],
                    'categoria':p[3],
                    'ganancia':float(p[0])*p[4]
                } for p in prod]
    return productos


def get_ventas_and_gastos_by_date(init, finish):
    '''Obtenemos las transacciones hechas (ventas y gastos) de manera
    histórica'''
    ganancias = db.session.query(
                        Venta.fecha.label('fecha_venta'), 
                        Transaccion.subtotal.label('subtotal_venta'),
                        literal(True).label('Gain?'),
                        TipoProducto.nombre,
                        Producto.nombre,
                        Categoria.nombre.label('extra')
                    )\
                    .join(Transaccion, Venta.referencia == Transaccion.id_referencia)\
                    .join(Precio, Transaccion.id_precio == Precio.id)\
                    .join(Producto, Producto.id == Precio.id_producto)\
                    .join(TipoProducto, TipoProducto.id == Precio.id_tipo_producto)\
                    .join(Categoria, Categoria.id == Producto.id_categoria)\
                    .filter(Venta.fecha.between(init, finish))\
    
    # WTF El join es después? 
    gastos = db.session.query(
                        Gasto.fecha.label('fecha_gasto'),
                        Gasto.cantidad.label('total_gasto'),
                        literal(False).label('Gain?'),
                        TipoGasto.nombre,
                        Gasto.nombre,
                        Gasto.nombre.label('extra')
                    )\
                    .join(TipoGasto, Gasto.id_tipo_gasto == TipoGasto.id)\
                    .filter(Gasto.fecha.between(init, finish))

    union = gastos.union_all(ganancias).order_by(desc('fecha_gasto'))

    historial = [{
                    'extra': p[5],
                    'nombre':p[4],
                    'tipo': p[3],
                    'gain': p[2],
                    'cantidad':p[1],
                    'fecha':p[0]
                } for p in union]
    
    return historial, len(union.all())



def add_transaction(transaction):
    '''Añade esta transaccion a la base de datos. Si existe lo reemplaza?
    La transaccion debe tener todos sus atributos ya definidos.'''
    db.session.add(transaction) #Añadir
    db.session.commit()     #Guardar y actualizar


### Ventas
def get_total_ventas():
    '''Suma total de todas las ventas'''
    return db.session.query(func.sum(Venta.total)).scalar()

def get_daily_total_ventas(today):
    '''Obtiene el total de ventas hechas en un día'''
    tomorrow = today + datetime.timedelta(days=1)
    tomorrow = tomorrow.replace(hour=23, minute=59, second=59)
    today = today.replace(hour=0, minute=0, second=0)
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
    '''Obtiene el numero de la última referencia'''
    return db.session.query(func.max(Venta.referencia)).scalar()

