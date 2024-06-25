# Import the entity to read as Entity object
from cafeteria_alina.model.categoria import Categoria

# Import the database
from cafeteria_alina import db


def get_categoria_by_name(nombre):
    '''Regresa todos los tipos de producto disponibles por producto'''
    return Categoria.query.filter(Categoria.nombre == nombre).first()

def get_all_categorias():
    return Categoria.query.all()

def add_categoria(precio):
    db.session.add(precio)
    db.session.commit()