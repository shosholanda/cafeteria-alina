#Import el usuario con sus atributos como objetox
from src.model.usuario import Usuario
from src.model.tipo_usuario import TipoUsuario
from src.model.sucursal import Sucursal

#Importar la base de datos.
from src import db

def get_usuario(correo):
    '''Obtiene un usuario dado su correo.'''
    return Usuario.query.get(correo)

def get_usuario_and_tipo(correo):
    '''Obtiene un usuario dado su correo.'''
    return Usuario.query\
        .join(TipoUsuario, TipoUsuario.id == Usuario.id_tipo_usuario)\
        .filter(Usuario.correo == correo).first()

def get_full_usuario(correo):
    '''Obtiene el usuario juntando la información de tipo_usuario y sucursal'''
    return Usuario.query\
        .join(TipoUsuario, TipoUsuario.id == Usuario.id_tipo_usuario)\
        .join(Sucursal, Sucursal.id == Usuario.id_sucursal)\
        .filter(Usuario.correo == correo).first()

def add_usuario(usuario):
    '''Añade este usuario a la base de datos. Si existe lo reemplaza?
    El usuario debe tener todos sus atributos ya definidos.'''
    db.session.add(usuario) #Añadir
    db.session.commit()     #Guardar y actualizar

def get_all_tipo_usuario():
    '''Regresa todos los tipos de usuario disponibles'''
    return TipoUsuario.query.all()
