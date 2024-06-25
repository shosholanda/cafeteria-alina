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
    #PK
    id = db.Column('id', db.Integer, primary_key = True)
    # Numero de referencia
    referencia = db.Column(db.Integer, db.ForeignKey('venta.referencia'))
    # Producto en cuestión
    id_producto = db.Column(db.Integer, db.ForeignKey('producto.id'))
    # tipo del producto
    # AAAAAA
    tipo = db.Column(db.Integer, db.ForeignKey('tipo_producto.id'))
    # Precio producto
    precio = db.Column('precio', db.Integer, nullable = False)
    # Cantidad de productos
    cantidad = db.Column('cantidad', db.Integer, nullable = False)
    # Subtotal
    subtotal = db.Column('subtotal', db.Integer, nullable = False)

    # Backref


    # Constructor
    def __init__(self,
                 referencia,
                 id_producto,
                 tipo,
                 precio,
                 cantidad,
                 subtotal):
        self.referencia = referencia
        self.id_producto = id_producto
        self.tipo = tipo
        self.precio = precio
        self.cantidad = cantidad
        self.subtotal = subtotal

    # Representación en cadena
    def __repr__(self) -> str:
        return f'{self.referencia} : {self.id_producto.nombre} - {self.cantidad}'
