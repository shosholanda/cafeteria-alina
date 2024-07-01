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
    # id del producto, ya trae la categoria
    id_producto = db.Column(db.Integer, db.ForeignKey('producto.id'))
    # id del tipo 
    id_tipo_producto = db.Column(db.Integer, db.ForeignKey('tipo_producto.id'))
    # Precio del producto. Debe ser consistente con el tipo
    precio = db.Column('precio', db.Float(2), nullable = False)
    # Nos dice si sigue estando activo o no el producto. Por omisión está activo
    status = db.Column('status', db.Boolean, nullable = False, default=True)


    ## Transaccion
    transaccion = db.relationship('Transaccion', back_populates='precio')

    ## Atributos 1 a muchos
    producto = db.relationship('Producto', back_populates = 'precios')
    tipo_producto = db.relationship('TipoProducto', back_populates = 'precio', uselist=False )

    # Constructor
    def __init__(self,
                 id_categoria,
                 id_producto,
                 id_tipo_producto,
                 precio):
        self.id_categoria = id_categoria
        self.id_producto = id_producto
        self.id_tipo_producto = id_tipo_producto
        self.precio = precio

    # Representación en cadena
    def __repr__(self) -> str:
        return f'{self.producto.categoria.nombre} | {self.producto.nombre} - {self.tipo_producto.nombre} : ${self.precio}'
    
    def category_and_name(self) -> str:
        return f'{self.producto.nombre}'
