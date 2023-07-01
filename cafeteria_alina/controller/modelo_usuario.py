#Import el usuario con sus atributos como objetox
from entity.usuario import Usuario

#Importar la base de datos.
from entity.__init__ import db

def get_usuario(email):
    '''Obtiene un usuario dado su email.'''
    return Usuario.query.filter(Usuario.email == email ).first()

def validar_usuario(email, password):
    '''Nos dice si el email y la contraseña son válidos en la bdd'''
    return Usuario.query.filter(Usuario.email == email, Usuario.password == password).first()

def crear_usuario(usuario):
    '''Añade este usuario a la base de datos. Si existe lo reemplaza?
    El usuario debe tener todos sus atributos ya definidos.'''
    db.session.add(usuario) #Añadir
    db.session.commit()     #Guardar y actualizar
