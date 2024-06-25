from cafeteria_alina import db
#WTF tengo q importar esta madres
from cafeteria_alina.model.tipo_producto import TipoProducto
from cafeteria_alina.model.categoria import Categoria
from cafeteria_alina.model.precio import Precio

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
    # Nombre del producto puesto por el usuario
    nombre = db.Column('nombre', db.String(100), nullable = False)
    # Descripción del producto (opcional)
    descripcion  = db.Column('descripcion', db.String(140), default = 'Sin descripción')
    # Categoria a la que pertenece ## PTM se rompio id_categoria
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'))
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
        self.categoria_id = id_categoria

    # Representación en cadena
    def __repr__(self) -> str:
        return f'{self.nombre}: {self.descripcion}'
