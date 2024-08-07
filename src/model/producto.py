from src import db
#WTF tengo q importar esta madres
from src.model.tipo_producto import TipoProducto
from src.model.categoria import Categoria
from src.model.precio import Precio

class Producto(db.Model):
    '''
    Clase que modela una entidad con sus respectivos atributos.

    Entidad: Producto
    Nos dice las características de un producto por separado.
    '''
    
    # Nombre de la tabla
    __tablename__ = 'producto'

    # PK
    id = db.Column('id', db.Integer, primary_key = True )
    # Categoria a la que pertenece ## PTM se rompio id_categoria
    id_categoria = db.Column(db.Integer, db.ForeignKey('categoria.id'))
    # Nombre del producto puesto por el usuario
    nombre = db.Column('nombre', db.String(100), nullable = False)
    # Descripción del producto (opcional)
    descripcion  = db.Column('descripcion', db.String(140), default = 'Sin descripción')
    # Nos dice si sigue estando activo o no el producto. Por omisión está activo
    status = db.Column('status', db.Boolean, nullable = False, default=True)
 
    ## Pertenecer
    categoria = db.relationship('Categoria', back_populates = 'productos')
    precios = db.relationship('Precio', back_populates = 'producto')

    # Constructor
    def __init__(self,
                 nombre,
                 descripcion,
                 id_categoria):
        self.nombre = nombre
        self.descripcion = descripcion
        self.id_categoria = id_categoria

    # Representación en cadena
    def __repr__(self) -> str:
        return f'{self.nombre}: {self.descripcion}'
    
    def prod_and_cat(self):
        return f'{self.nombre} - {self.categoria.nombre}'
