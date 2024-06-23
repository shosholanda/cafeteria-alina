#Import el usuario con sus atributos como objetox
from cafeteria_alina.model.venta import Venta
from cafeteria_alina.model.transaccion import Transaccion
#Importar la base de datos.
from cafeteria_alina import db

from sqlalchemy import func

#Importar la base de datos.
from cafeteria_alina import db

def get_all_transactions():
    '''Obtiene todas las transacciones'''
    return Transaccion.query.all()
    

def get_last_ref():
    '''Obtiene el número de la última referencia'''
    return db.session.query(func.max(Venta.referencia)).scalar()

def add_transaction(transaction):
    '''Añade esta transaccion a la base de datos. Si existe lo reemplaza?
    La transaccion debe tener todos sus atributos ya definidos.'''
    db.session.add(transaction) #Añadir
    db.session.commit()     #Guardar y actualizar
