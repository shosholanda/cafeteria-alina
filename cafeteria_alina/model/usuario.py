from cafeteria_alina import db
from cafeteria_alina.model.tipo_usuario import *

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
    #Se guarda como hash. Fixed size = 102
    contraseña = db.Column('contraseña', db.String(102), nullable = False)
    # Fecha de nacimiento del trabajador
    fecha_nacimiento = db.Column('fecha_nacimiento', db.Date, nullable = False)
    # Privilegios del trabajador
    tipo = db.Column(db.Integer, db.ForeignKey('tipo_usuario.id'))
    # Nos dice si sigue estando activo o no el trabajador. Por omisión está activo
    status = db.Column('status', db.Boolean, nullable = False, default=True)

    ## Registrar
    sucursal = db.relationship('Sucursal', back_populates = 'usuarios')

    # Constructor
    def __init__(self,
                 correo,
                 contraseña,
                 nombre,
                 apellido_paterno,
                 apellido_materno,
                 tipo,
                 fecha_nacimiento):
        self.correo = correo
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.tipo = tipo
        self.contraseña = contraseña
        self.fecha_nacimiento = fecha_nacimiento

    # Representación en cadena
    def __repr__(self) -> str:
        return f'id: {self.correo}'

