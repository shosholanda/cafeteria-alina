from cafeteria_alina import db

class Transaccion(db.Model):
    '''
    Clase que modela una entidad con sus respectivos atributos.

    Entidad: Transacción
    La transacción tiene información de los productos vendidos en una
    exhibicion
    '''

    # Nombre de la tabla
    __tablename__ = 'transaccion'
    # Numero de referencia
    referencia = db.Column(db.Integer, db.ForeignKey('venta.referencia'))
    # Producto en cuestión
    id_producto = db.Column(db.Integer, db.ForeignKey('producto.id_producto'))
    # Precio producto
    precio = db.Column('precio', db.Integer, nullable = False)
    # Cantidad de productos
    cantidad = db.Column('cantidad', db.Integer, nullable = False)
    # Subtotal
    subtotal = db.Column('subtotal', db.Integer, nullable = False)


    # Constructor
    def __init__(self,
                 id_producto,
                 referencia,
                 cantidad):
        self.id_producto = id_producto
        self.referencia = referencia
        self.cantidad = cantidad

    # Representación en cadena
    def __repr__(self) -> str:
        return f'{self.referencia} : {self.id_producto.nombre} - {self.cantidad}'
