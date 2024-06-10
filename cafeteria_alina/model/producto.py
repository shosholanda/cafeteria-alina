from cafeteria_alina import db

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
    # Precio del producto. Debe ser consistente con el tamaño
    precio = db.Column('precio', db.Integer(3), nullable = False)
    # Tamaño del producto. No hay producto sin tamaño
    tamaño = db.Column(db.Integer, db.ForeignKey('tamaño.id_tamaño'))
    # Descripción del producto (opcional)
    descripcion  = db.Column('descripcion', db.String(140), default = 'Sin descripción')
    # Nos dice si sigue estando activo o no el producto. Por omisión está activo
    status = db.Column('status', db.Boolean, nullable = False, default=True)

    # Constructor
    def __init__(self,
                 id_producto,
                 nombre,
                 precio,
                 descripcion):
        
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

    # Representación en cadena
    def __repr__(self) -> str:
        return f'{self.nombre} - {self.tamaño} : ${self.precio}'
