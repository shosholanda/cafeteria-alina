#Import el usuario con sus atributos como objetox
from cafeteria_alina.model.usuario import Usuario
from cafeteria_alina.model.tipo_usuario import TipoUsuario
from cafeteria_alina.model.sucursal import Sucursal

#Importar la base de datos.
from cafeteria_alina import db

def get_usuario(correo):
    '''Obtiene un usuario dado su correo.'''
    return Usuario.query.filter(Usuario.correo == correo ).first()

def get_full_usuario(correo):
    '''Obtiene el usuario juntando la información de tipo_usuario y sucursal'''
    # AAA
    return Usuario.query\
        .filter(Usuario.correo == correo)\
        .join(TipoUsuario, TipoUsuario.id == Usuario.tipo_usuario)\
        .join(Sucursal, Sucursal.id_sucursal == Usuario.id_sucursal).first()

def add_usuario(usuario):
    '''Añade este usuario a la base de datos. Si existe lo reemplaza?
    El usuario debe tener todos sus atributos ya definidos.'''
    db.session.add(usuario) #Añadir
    db.session.commit()     #Guardar y actualizar

def get_all_tipo_usuario():
    '''Regresa todos los tipos de usuario disponibles'''
    return TipoUsuario.query.all()