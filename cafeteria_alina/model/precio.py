from cafeteria_alina import db
#WTF tengo q importar esta madres
from cafeteria_alina.model.tipo_producto import TipoProducto

class Precio(db.Model):
    '''
    Clase que modela una entidad con sus respectivos atributos.

    Entidad: Precio
    Reune un producto, su tipo y le asocia un precio
    '''

    # Nombre de la tabla
    __tablename__ = 'precio'

    # PK
    id = db.Column('id', db.Integer, primary_key = True )
    # id del producto 
    id_producto = db.Column(db.Integer, db.ForeignKey('producto.id'))
    # id del tipo 
    id_tipo = db.Column(db.Integer, db.ForeignKey('tipo_producto.id'))
    # Precio del producto. Debe ser consistente con el tipo
    precio = db.Column('precio', db.Integer, nullable = False)
    
    # Nos dice si sigue estando activo o no el producto. Por omisión está activo
    status = db.Column('status', db.Boolean, nullable = False, default=True)

    ## acceder a estas tablas desde aquí
    producto = db.relationship('Producto', back_populates = 'precios')
    ## Regresa el objeto relacionado a este tipo
    tipo = db.relationship('TipoProducto', back_populates = 'nombre_tipo')

    # Constructor
    def __init__(self,
                 id_producto,
                 id_tipo,
                 precio):
        self.id_producto = id_producto
        self.id_tipo = id_tipo
        self.precio = precio

    # Representación en cadena
    def __repr__(self) -> str:
        return f'{self.producto.nombre} - {self.tipo.tipo} : ${self.precio}'
