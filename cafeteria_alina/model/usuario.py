from entity.__init__ import db


class Usuario(db.Model):

    __tablename__ = 'usuario'
    email = db.Column('email', db.String(100), primary_key = True)
    password = db.Colum('password', db.String(40))
    nombre = db.Column('nombre', db.String(100))
    apellido = db.Colum('apellido', db.String(100))
    fecha_nacimiento = db.Column('fecha_nacimiento', db.Date)
    tipo_usuario = db.Column('tipo_usuario', db.ForeignKey('tipo_usuario'), nullable = False)
    salario = db.Column('salario', db.Float)
    status = db.Column('status', db.Boolean, default=True)


    #Usuario completo
    def __init__(self,
                 email,
                 password,
                 nombre,
                 apellido,
                 fecha_nacimiento,
                 tipo_usuario,
                 salario)
        self.email = email
        self.passwd = password
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.tipo_usuario = tipo_usuario
        self.salario = salario

    # String representation
    def __repr__(self) -> str:
        return f'id: {email}'

