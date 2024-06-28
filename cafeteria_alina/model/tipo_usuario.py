from cafeteria_alina import db

class TipoUsuario(db.Model):
    '''
    Clase que modela una entidad con sus respectivos atributos.

    Entidad: Tipo
    Los diferentes Tipos de usuario
    '''

    # Nombre de la tabla
    __tablename__ = 'tipo_usuario'
    # PK
    id = db.Column('id', db.Integer, primary_key = True)
    # Tipo del tipo completo
    nombre = db.Column('nombre', db.String(20), nullable = False)
    # Nos dice si sigue estando activo o no el trabajador. Por omisión está activo
    status = db.Column('status', db.Boolean, nullable = False, default=True)

    ## acceder a esta tabla desde usuario
    usuario = db.relationship('Usuario', back_populates = 'tipo_usuario', uselist=False)

    # Constructor
    def __init__(self,
                 nombre):
        self.nombre = nombre
                 

    # Representación en cadena
    def __repr__(self) -> str:
        return f'tipo: {self.nombre}'

