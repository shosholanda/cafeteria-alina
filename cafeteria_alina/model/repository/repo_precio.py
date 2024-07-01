# Import the entity to read as Entity object
from cafeteria_alina.model.producto import Producto
from cafeteria_alina.model.tipo_producto import TipoProducto
from cafeteria_alina.model.precio import Precio

# Import the database
from cafeteria_alina import db


def get_tipos_por_producto_available(id_producto):
    '''Regresa todos los tipos de producto disponibles por producto'''
    return Precio.query\
            .join(TipoProducto, TipoProducto.id == Precio.id_tipo_producto)\
            .join(Producto, Producto.id == Precio.id_producto)\
            .filter(Producto.id == id_producto)


def get_all_avaliable_precios():
    '''Leer todos los precios que no hayan sido eliminados'''
    return Precio.query.filter(Precio.status == 1)

def get_all_avaliable_precios_by(columna):
    '''Lo mismo pero ordenados'''
    results = get_all_avaliable_precios()\
        .join(Producto, Precio.id_producto == Producto.id)\
        .filter(Producto.status == 1)
    
    if columna == 'PRODUCTO':
        return results.order_by(Precio.id_producto)
    if columna == 'TIPO':
        return results.order_by(Precio.id_tipo_producto)
    if columna == 'PRECIO':
        return results.order_by(Precio.precio)
    if columna == 'NOMBRE':
        return results.order_by(Producto.nombre)
    return results

def get_all_precios():
    '''Leer todos los precios que no hayan sido eliminados'''
    return Precio.query.all()


def add_precio(precio):
    db.session.add(precio)
    db.session.commit()

def get_all_tipos(id_producto):
    '''Lee todos los precios de cierto producto'''
    return Precio.query.filter(Precio.id_producto == id_producto)
    
def get_precio_unico(id_producto, id_tipo_producto):
    '''Nos da el precio por el id_producto y id_tipo_producto único'''
    return Precio.query\
        .join(Producto, Precio.id_producto == Producto.id)\
        .join(TipoProducto, Precio.id_tipo_producto == TipoProducto.id)\
        .filter(Precio.id_producto == id_producto, Precio.id_tipo_producto == id_tipo_producto)\
        .first()

def hide_precio(precio):
    '''soft delete'''
    if precio:
        precio.status = 0
        add_precio(precio)
    else:
        return "hubo un error"

def remove_precio(precio):
    '''No hay vuelta atrás'''
    db.session.delete(precio)
    db.session.commit()
    
