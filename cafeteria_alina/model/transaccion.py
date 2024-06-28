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
    id_referencia = db.Column(db.Integer, db.ForeignKey('venta.referencia'))
    # Producto relacionado a esta transaccion
    id_precio = db.Column(db.Integer, db.ForeignKey('precio.id'))
    # Cantidad de productos
    cantidad = db.Column('cantidad', db.Integer, nullable = False)
    # Subtotal
    subtotal = db.Column('subtotal', db.Float(2), nullable = False)

    
    precio = db.relationship('Precio', back_populates='transaccion')


    # Constructor
    def __init__(self,
                 id_referencia,
                 id_precio,
                 cantidad,
                 subtotal):
        self.id_referencia = id_referencia
        self.id_precio = id_precio
        self.cantidad = cantidad
        self.subtotal = subtotal

    # Representación en cadena
    def __repr__(self) -> str:
        return f'{self.id_referencia} : {self.id_producto.nombre} - {self.cantidad}'
