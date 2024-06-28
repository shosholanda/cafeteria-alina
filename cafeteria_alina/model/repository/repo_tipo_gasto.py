#Importar la base de datos.
from cafeteria_alina import db

#Import el usuario con sus atributos como objetox
from cafeteria_alina.model.tipo_gasto import TipoGasto


def get_all_tipo_gasto():
    '''Obtiene todos los gastos de la base de datos'''
    return TipoGasto.query.all()

def get_all_available_tipo_gasto():
    '''Obtiene todos los gastos disponibles de la base de datos'''
    return TipoGasto.query.filter(TipoGasto.status == 1)

def get_tipo_gasto_by_id(id):
    '''Obtiene el que coincide por id'''
    return TipoGasto.query.get(id)

def get_tipo_gasto_by_name(nombre):
    '''Obtiene el que coincide por nombre'''
    return TipoGasto.query.filter(TipoGasto.nombre == nombre).first()

def get_by_tipo(tipo):
    '''Obtiene el que coincide por cadena'''
    return TipoGasto.query.filter(TipoGasto.tipo == tipo).first()

def add_tipo_gasto(tipo):
    '''Añade este tipo a la base de datos. Si existe lo reemplaza?
    El tipo debe tener todos sus atributos ya definidos.'''
    db.session.add(tipo)
    db.session.commit()

def hide_tipo_gasto(tipo):
    '''Añade este tipo a la base de datos. Si existe lo reemplaza?
    El tipo debe tener todos sus atributos ya definidos.'''
    tipo.status = 0
    add_tipo_gasto(tipo)
