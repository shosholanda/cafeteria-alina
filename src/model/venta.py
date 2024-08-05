import datetime
from src import db

class Venta(db.Model):
    '''
    Clase que modela una entidad con sus respectivos atributos.

    Entidad: Venta
    La venta tiene información sobre las transacciones que se han hecho 
    con qué usuario y a qué sucursal.
    '''

    # Nombre de la tabla
    __tablename__ = 'venta'
    # PK
    referencia = db.Column('referencia', db.Integer, primary_key = True)
    # Usuario operador
    id_usuario = db.Column(db.String(100), db.ForeignKey('usuario.correo'))
    # Sucursal
    id_sucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'))
    # Total de la transacción aplicando el IVA
    total = db.Column('total', db.Float(2), nullable = False)
    # Fecha y hora de la transacción
    fecha  = db.Column('fecha', db.DateTime)

    #Venta.usuario => Usuario() & Usuario.ventas => Venta()
    usuario = db.relationship('Usuario', back_populates='ventas')
    sucursal = db.relationship('Sucursal', back_populates='ventas')

    # Constructor
    def __init__(self,
                 total,
                 id_usuario,
                 id_sucursal):
        self.total = total
        self.id_usuario = id_usuario
        self.id_sucursal = id_sucursal
        self.fecha = datetime.datetime.now()

    # Representación en cadena
    def __repr__(self) -> str:
        return f'{self.referencia} : ${self.total} - {self.fecha}'
