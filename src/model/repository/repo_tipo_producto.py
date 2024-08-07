#Importar la base de datos.
from src import db

#Import el usuario con sus atributos como objetox
from src.model.tipo_producto import TipoProducto


def get_all_tipo_producto():
    '''Obtiene todos los productos de la base de datos'''
    return TipoProducto.query.all()

def get_all_available_tipo_producto():
    '''Obtiene todos los productos disponibles de la base de datos'''
    return TipoProducto.query.filter(TipoProducto.status == 1)

def get_by_id(id):
    '''Obtiene el que coincide por id'''
    return TipoProducto.query.get(id)

def get_by_tipo(tipo):
    '''Obtiene el tipo de producto que coincide por cadena'''
    return TipoProducto.query.filter(TipoProducto.nombre == tipo).first()

def add_tipo_producto(tipo):
    '''Añade este tipo a la base de datos. Si existe lo reemplaza?
    El tipo debe tener todos sus atributos ya definidos.'''
    db.session.add(tipo) #Añadir
    db.session.commit()     #Guardar y actualizar
