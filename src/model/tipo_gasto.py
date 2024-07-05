from src import db

class TipoGasto(db.Model):
    '''
    Clase que modela una entidad con sus respectivos atributos.

    Entidad: Tipo
    Los diferentes Tipos de gasto
    '''

    # Nombre de la tabla
    __tablename__ = 'tipo_gasto'
    # PK
    id = db.Column('id', db.Integer, primary_key = True)
    # Tipo del tipo completo
    nombre = db.Column('nombre', db.String(50), nullable = False)
    # Descripcion del gasto
    descripcion = db.Column('descripcion', db.String(128), nullable = False)
    # Nos dice si sigue estando activo o no el tipo. Por omisión está activo
    status = db.Column('status', db.Boolean, nullable = False, default=True)

    ## acceder a esta tabla desde gasto
    gasto = db.relationship('Gasto', back_populates = 'tipo_gasto', uselist = False)

    # Constructor
    def __init__(self,
                 nombre,
                 descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
                 

    # Representación en cadena
    def __repr__(self) -> str:
        return f'tipo: {self.nombre}'

