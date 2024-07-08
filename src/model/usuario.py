from src import db
# WTF tengo q importar esa madre che flask pendejo
from src.model.tipo_usuario import TipoUsuario
from src.model.sucursal import Sucursal

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
    # Privilegios del trabajador    
    id_tipo_usuario = db.Column(db.Integer, db.ForeignKey('tipo_usuario.id'), nullable = False)
    # Sucursal a la que pertenece
    id_sucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'))
    # Nombre completo separado
    nombre = db.Column('nombre', db.String(100), nullable = False)
    apellido_paterno = db.Column('apellido_paterno', db.String(100), nullable = False)
    apellido_materno = db.Column('apellido_materno', db.String(100), nullable = False)
    #Se guarda como hash. Fixed size = 162
    contraseña = db.Column('contraseña', db.String(162), nullable = False)
    # Fecha de nacimiento del trabajador
    fecha_nacimiento = db.Column('fecha_nacimiento', db.Date, nullable = False)

    ## Registrar
    sucursal = db.relationship('Sucursal', back_populates = 'usuarios')
    ## Regresa el objeto relacionado a este tipo
    tipo_usuario = db.relationship('TipoUsuario', back_populates = 'usuario', uselist=False)
    ## Ventas registradas por este usuario
    ventas = db.relationship('Venta', back_populates = 'usuario')
    
    # Nos dice si sigue estando activo o no el trabajador. Por omisión está activo
    status = db.Column('status', db.Boolean, nullable = False, default=True)


    # Constructor
    def __init__(self,
                 id_tipo_usuario,
                 id_sucursal,
                 correo,
                 contraseña,
                 nombre,
                 apellido_paterno,
                 apellido_materno,
                 fecha_nacimiento):
        self.correo = correo
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.id_tipo_usuario = id_tipo_usuario
        self.id_sucursal = id_sucursal
        self.contraseña = contraseña
        self.fecha_nacimiento = fecha_nacimiento

    # Representación en cadena
    def __repr__(self) -> str:
        return f'id: {self.correo}'

