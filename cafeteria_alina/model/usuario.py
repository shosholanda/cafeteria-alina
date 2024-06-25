from cafeteria_alina import db
# WTF tengo q importar esa madre che flask pendejo
from cafeteria_alina.model.tipo_usuario import TipoUsuario
from cafeteria_alina.model.sucursal import Sucursal

class Usuario(db.Model):
    '''
    Clase que modela una entidad con sus respectivos atributos.

    Entidad: Usuario
    Los usuarios son los que operan las transacciones del negocio
    '''

    # Nombre de la tabla
    __tablename__ = 'usuario'
    # Correo electrónico del trabajador. Solo uno por usuario
    correo = db.Column('correo', db.String(100), primary_key = True)
    # Nombre completo separado
    nombre = db.Column('nombre', db.String(100), nullable = False)
    apellido_paterno = db.Column('apellido_paterno', db.String(100), nullable = False)
    apellido_materno = db.Column('apellido_materno', db.String(100), nullable = False)
    #Se guarda como hash. Fixed size = 162
    contraseña = db.Column('contraseña', db.String(162), nullable = False)
    # Fecha de nacimiento del trabajador
    fecha_nacimiento = db.Column('fecha_nacimiento', db.Date, nullable = False)
    # Privilegios del trabajador    
    tipo_usuario = db.Column(db.Integer, db.ForeignKey('tipo_usuario.id'))
    # Sucursal a la que pertenece
    id_sucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id_sucursal'))

    ## Registrar
    sucursal = db.relationship('Sucursal', back_populates = 'usuarios')
    ## Regresa el objeto relacionado a este tipo
    tipo = db.relationship('TipoUsuario', back_populates = 'usuario', uselist=False)
    
    # Nos dice si sigue estando activo o no el trabajador. Por omisión está activo
    status = db.Column('status', db.Boolean, nullable = False, default=True)


    # Constructor
    def __init__(self,
                 correo,
                 contraseña,
                 nombre,
                 apellido_paterno,
                 apellido_materno,
                 tipo_usuario,
                 fecha_nacimiento):
        self.correo = correo
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.tipo_usuario = tipo_usuario
        self.contraseña = contraseña
        self.fecha_nacimiento = fecha_nacimiento

    # Representación en cadena
    def __repr__(self) -> str:
        return f'id: {self.correo}'

