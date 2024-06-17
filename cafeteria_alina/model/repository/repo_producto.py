# Import the entity to read as Entity object
from cafeteria_alina.model.producto import Producto
from cafeteria_alina.model.precio import Precio

# Import the database
from cafeteria_alina import db


def get_producto(nombre):
    '''Regresa un producto de la base de datos por cadena'''
    return Producto.query.filter(Producto.nombre == nombre).first()


def get_producto_id(id):
    '''Regresa un producto más en especifico dado su id'''
    return Producto.query.filter(Producto.id == id).first()

def agregar_producto(producto):
    '''Agrega un nuevo producto a la base de datos (CREATE)'''
    db.session.add(producto)
    db.session.commit()

def read_productos():
    '''Regresa todos los productos disponibles'''
    productos = Producto.query.filter(Producto.status == 1)
    return productos

def eliminar_producto(producto):
    '''"Elimina" El producto de la lista de productos. En realidad, solamente se apaga el status,
    siempre se conserva en la bdd'''
    producto.status = 0
    agregar_producto(producto)


### Precios
def get_all_avaliable_precios():
    '''Leer todos los precios que no hayan sido eliminados'''
    return Precio.query.filter(Precio.status == 1 and Precio.nombre != None)


def agregar_precio(precio):
    db.session.add(precio)
    db.session.commit()

def read_precios(id_precio):
    '''Lee todos los precios de cierto producto'''
    return Precio.query.filter(Precio.id_precio == id_precio)
    
def get_precio_unico(id_producto, id_tipo):
    '''Nos da el precio por el id_producto y id_tipo único'''
    return Precio.query.filter(Precio.id_producto == id_producto, Precio.id_tipo == id_tipo).first()

def eliminar_precio(precio):
    db.session.delete(precio)
    db.session.commit()
    




