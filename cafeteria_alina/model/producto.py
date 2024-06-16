from cafeteria_alina import db
#WTF tengo q importar esta madres
from cafeteria_alina.model.tipo_producto import TipoProducto
from cafeteria_alina.model.categoria import Categoria

class Producto(db.Model):
    '''
    Clase que modela una entidad con sus respectivos atributos.

    Entidad: Producto
    Nos dice las características de un producto por separado.
    '''
    
    # Nombre de la tabla
    __tablename__ = 'producto'

    # PK
    id_producto = db.Column('id_producto', db.Integer, primary_key = True )
    # Nombre del producto puesto por el usuario
    nombre = db.Column('nombre', db.String(100), nullable = False)
    # Precio del producto. Debe ser consistente con el tipo
    precio = db.Column('precio', db.Integer, nullable = False)
    # tipo del producto. No hay producto sin tipo
    tipo = db.Column(db.Integer, db.ForeignKey('tipo_producto.id'))
    # Descripción del producto (opcional)
    descripcion  = db.Column('descripcion', db.String(140), default = 'Sin descripción')
    # Nos dice si sigue estando activo o no el producto. Por omisión está activo
    status = db.Column('status', db.Boolean, nullable = False, default=True)

    # Necesario para la relacion
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'))
    ## Pertenecer
    categoria = db.relationship('Categoria', back_populates = 'productos')

    # Constructor
    def __init__(self,
                 nombre,
                 tamaño,
                 precio,
                 tipo,
                 descripcion):
        self.nombre = nombre
        self.tamaño = tamaño
        self.precio = precio
        self.tipo = tipo
        self.descripcion = descripcion

    # Representación en cadena
    def __repr__(self) -> str:
        return f'{self.nombre} - {self.tamaño} : ${self.precio}'
