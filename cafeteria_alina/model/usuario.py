from cafeteria_alina import db


class Usuario(db.Model):

    __tablename__ = 'usuario'
    correo = db.Column('correo', db.String(100), primary_key = True)
    #Se guarda como hash
    contraseña = db.Column('contraseña', db.String(102), nullable = False)
    nombre = db.Column('nombre', db.String(100), nullable = False)
    apellido_paterno = db.Column('apellido_paterno', db.String(100), nullable = False)
    apellido_materno = db.Column('apellido_materno', db.String(100), nullable = False)

    fecha_nacimiento = db.Column('fecha_nacimiento', db.Date, nullable = False)
    status = db.Column('status', db.Boolean, nullable = False, default=True)


    #Usuario completo
    def __init__(self,
                 correo,
                 contraseña,
                 nombre,
                 apellido_paterno,
                 apellido_materno,
                 fecha_nacimiento):
        self.correo = correo
        self.contraseña = contraseña
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.fecha_nacimiento = fecha_nacimiento

    # String representation
    def __repr__(self) -> str:
        return f'id: {self.correo}'

