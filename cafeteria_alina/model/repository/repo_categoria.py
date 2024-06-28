# Import the entity to read as Entity object
from cafeteria_alina.model.categoria import Categoria
from cafeteria_alina.model.producto import Producto

# Import the database
from cafeteria_alina import db


def get_categoria_by_name(nombre):
    '''Regresa la categoria única por nombre'''
    return Categoria.query.filter(Categoria.nombre == nombre).first()

def get_categorias_by_product_id(id_producto):
    '''Regresa las categorias que coincidan con el producto'''
    product = Producto.query.get(id_producto)
    return Categoria.query\
        .join(Producto, Producto.id_categoria == Categoria.id)\
        .filter(Producto.nombre == product.nombre)
    

def get_all_categorias():
    return Categoria.query.all()

def add_categoria(precio):
    db.session.add(precio)
    db.session.commit()