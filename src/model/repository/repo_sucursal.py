# Import the entity to read as Entity object
from src.model.sucursal import Sucursal

# Import the database
from src import db


def get_all_sucursales():
    '''Regresa todos los tipos de producto disponibles por producto'''
    return Sucursal.query.all()

def get_all_available_sucursales():
    return Sucursal.query.filter(Sucursal.status == 1)

def get_sucursal_by_id(id):
    '''Regresamos la sucursal por id'''
    return Sucursal.query.get(id)

def get_sucursal_by_nombre(nombre):
    '''Regresamos la sucursal por nombre'''
    return Sucursal.query.filter(Sucursal.nombre == nombre).first()

def add_sucursal(sucursal):
    db.session.add(sucursal)
    db.session.commit()

def hide_sucursal(sucursal):
    sucursal.status = 0
    add_sucursal(sucursal)
