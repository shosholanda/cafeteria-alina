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
    tipo = db.Column('tipo', db.String(20), nullable = False)
    # Nos dice si sigue estando activo o no el trabajador. Por omisión está activo
    status = db.Column('status', db.Boolean, nullable = False, default=True)

    # Constructor
    def __init__(self,
                 tipo):
        self.tipo = tipo
                 

    # Representación en cadena
    def __repr__(self) -> str:
        return f'tipo: {self.tipo}'

