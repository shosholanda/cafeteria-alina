#Import el usuario con sus atributos como objetox
from model.usuario import Usuario

#Importar la base de datos.
from model import db

def get_usuario(correo):
    '''Obtiene un usuario dado su correo.'''
    return Usuario.query.filter(Usuario.correo == correo ).first()

def validar_usuario(correo, contraseña):
    '''Nos dice si el correo y la contraseña son válidos en la bdd'''
    return Usuario.query.filter(Usuario.correo == correo, Usuario.contraseña == contraseña).first()

def crear_usuario(usuario):
    '''Añade este usuario a la base de datos. Si existe lo reemplaza?
    El usuario debe tener todos sus atributos ya definidos.'''
    db.session.add(usuario) #Añadir
    db.session.commit()     #Guardar y actualizar
