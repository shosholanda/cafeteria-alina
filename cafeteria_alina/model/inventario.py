from cafeteria_alina import db

class Inventario(db.Model):
    '''
    Clase que modela una entidad con sus respectivos atributos.

    Entidad: Inventario
    Nos da los productos que tenemos en stock
    '''

    # Nombre de la tabla
    __tablename__ = 'Inventario'
    # PK
    id_producto = db.Column(db.Integer, db.ForeignKey('insumo.gtin'))
    # Usuario comprador
    usuario = db.Column(db.String, db.ForeignKey('usuario.correo'))
    # Precio del producto.
    precio = db.Column('precio', db.Float, nullable = False)
    # Descripción del Inventario (opcional)
    stock = db.Column('stock', db.Integer, nullable = False)

    # Constructor
    def __init__(self,
                 stock,
                 precio):
       self.stock = stock
       self.precio = precio

    # Representación en cadena
    def __repr__(self) -> str:
        return f'{self.id_producto.nombre} - ${self.precio} - {self.stock}'