# Import the entity to read as Entity object
from cafeteria_alina.model.producto import Producto
from cafeteria_alina.model.tipo_producto import TipoProducto
from cafeteria_alina.model.precio import Precio

# Import the database
from cafeteria_alina import db


def get_tipos_por_producto_available(id):
    '''Regresa todos los tipos de producto disponibles por producto'''
    return Precio.query\
                .join(TipoProducto, Precio.id_tipo == TipoProducto.id)\
                .filter(Precio.id_producto == id)
