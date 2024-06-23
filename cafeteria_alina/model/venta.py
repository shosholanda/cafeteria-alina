import datetime
from cafeteria_alina import db

class Venta(db.Model):
    '''
    Clase que modela una entidad con sus respectivos atributos.

    Entidad: Venta
    La venta tiene información sobre las transacciones que se han hecho 
    con qué usuario.
    '''

    # Nombre de la tabla
    __tablename__ = 'venta'
    # PK
    referencia = db.Column('referencia', db.Integer, primary_key = True)
    # Total de la transacción aplicando el IVA
    total = db.Column('total', db.Integer, nullable = False)
    # Fecha y hora de la transacción
    fecha  = db.Column('fecha', db.DateTime, default = datetime.datetime.now())
    # Usuario operador
    usuario = db.Column(db.String(100), db.ForeignKey('usuario.correo'))
    # Sucursal
    #sucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id_sucursal'))

    # Constructor
    def __init__(self,
                 total,
                 usuario):
        self.total = total
        self.usuario = usuario

    # Representación en cadena
    def __repr__(self) -> str:
        return f'{self.referencia} : {self.total} - {self.fecha}'
