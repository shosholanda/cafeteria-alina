# Import the entity to read as Entity object
from src.model.producto import Producto
from src.model.precio import Precio

# Import the database
from src import db


def get_producto(nombre):
    '''Regresa un producto de la base de datos por cadena'''
    return Producto.query.filter(Producto.nombre == nombre).first()

def get_producto_and_categoria(nombre, categoria):
    # AAA debemos buscar producto que coincida por grupo y producto
    '''Regresa un producto de la base de datos por cadena'''
    return Producto.query.filter(Producto.nombre == nombre, Producto.id_categoria == categoria).first()

def get_producto_id(id):
    '''Regresa un producto más en especifico dado su id'''
    return Producto.query.get(id)

def agregar_producto(producto):
    '''Agrega un nuevo producto a la base de datos (CREATE)'''
    db.session.add(producto)
    db.session.commit()

def get_ordered_productos_by_name():
    return Producto.query.filter(Producto.status == 1)\
        .order_by(Producto.nombre)

def get_all_available_productos():
    '''Regresa todos los productos disponibles'''
    productos = Producto.query.filter(Producto.status == 1)
    return productos.order_by(Producto.id)

def get_all_available_productos_inverse():
    '''Regresa todos los productos disponibles'''
    productos = Producto.query.filter(Producto.status == 1)
    return productos.order_by(-Producto.id)

def hide_producto(producto):
    '''soft delete'''
    if producto:
        producto.status = 0
        agregar_producto(producto)
    else:
        return "hubo un error"

def remove_producto(producto):
    '''No hay vuelta atrás'''
    db.session.delete(producto)
    db.session.commit()



