# Import the entity to read as Entity object
from entity.producto import Producto

# Import the database
from entity.__init__ import db


def get_producto(nombre):
    '''Regresa un producto de la base de datos cuya medida es 0'''
    return Producto.query.filter(Producto.nombre == nombre)


def get_producto_id(id_producto):
    '''Regresa un producto más en especifico dado su id (gtin)'''
    return Producto.query.filter(Producto.id_producto = id_producto)
