#Import el usuario con sus atributos como objetox
from cafeteria_alina.model.usuario import Usuario

#Importar la base de datos.
from cafeteria_alina import db

def get_usuario(correo):
    '''Obtiene un usuario dado su correo.'''
    return Usuario.query.filter(Usuario.correo == correo ).first()

def crear_usuario(usuario):
    '''Añade este usuario a la base de datos. Si existe lo reemplaza?
    El usuario debe tener todos sus atributos ya definidos.'''
    db.session.add(usuario) #Añadir
    db.session.commit()     #Guardar y actualizar