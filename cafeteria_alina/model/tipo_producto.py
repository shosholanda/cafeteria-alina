from cafeteria_alina import db

class TipoProducto(db.Model):
    '''
    Clase que modela una entidad con sus respectivos atributos.

    Entidad: Tipo
    Los diferentes Tipos para los diferentes precios
    '''

    # Nombre de la tabla
    __tablename__ = 'tipo_producto'
    # PK
    id = db.Column('id', db.Integer, primary_key = True)
    # Tipo del tipo completo
    nombre = db.Column('nombre', db.String(20), nullable = False)
    # Nos dice si sigue estando activo o no el tipo. Por omisión está activo
    status = db.Column('status', db.Boolean, nullable = False, default=True)

    ## acceder a esta tabla desde precio
    precio = db.relationship('Precio', back_populates = 'tipo_producto', uselist = False)

    # Constructor
    def __init__(self,
                 nombre):
        self.nombre = nombre
                 

    # Representación en cadena
    def __repr__(self) -> str:
        return f'tipo: {self.nombre}'

