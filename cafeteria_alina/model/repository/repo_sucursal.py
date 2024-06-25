# Import the entity to read as Entity object
from cafeteria_alina.model.sucursal import Sucursal

# Import the database
from cafeteria_alina import db


def get_all_sucursales():
    '''Regresa todos los tipos de producto disponibles por producto'''
    return Sucursal.query.all()

def get_sucursal_by_id(id):
    '''Regresamos la sucursal por id'''
    # AAA
    return Sucursal.query.filter(Sucursal.id_sucursal == id).first()

def add_sucursal(sucursal):
    db.session.add(sucursal)
    db.session.commit()

def hide_sucursal(id):
    sucursal = get_sucursal_by_id(id)
    sucursal.status = 0
    add_sucursal(sucursal)
