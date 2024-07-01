import datetime
from cafeteria_alina import db

class Gasto(db.Model):
    '''
    Clase que modela una entidad con sus respectivos atributos.

    Entidad: Gasto
    Guarda todos los gastos hechos para esta sucursal
    '''

    # Nombre de la tabla
    __tablename__ = 'gasto'
    # PK
    id = db.Column('id', db.Integer, primary_key = True)
    # Tipo de gasto:
    id_tipo_gasto = db.Column(db.Integer, db.ForeignKey('tipo_gasto.id'))
    # Gasto asociado a la sucursal
    id_sucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'))
    # Nombre del gasto: Ej. Luz, Insumos
    nombre = db.Column('nombre', db.String(50), nullable = False)
    # Gasto
    cantidad = db.Column('cantidad', db.Float(2), nullable = False)
    # Fecha 
    fecha = db.Column('fecha', db.DateTime, default = datetime.datetime.now())
    # Status
    status = db.Column('status', db.Boolean, default = True)

    # Todos los tipos de gastos relacionados a este gasto
    tipo_gasto = db.relationship('TipoGasto', back_populates = 'gasto', uselist = False)
    # Todos los gastos relacionados al id_sucursal seleccionado
    sucursal = db.relationship('Sucursal', back_populates = 'gastos')


    # Constructor
    def __init__(self,
                 id_sucursal,
                 nombre,
                 id_tipo_gasto,
                 cantidad):
        self.id_sucursal = id_sucursal
        self.nombre = nombre
        self.id_tipo_gasto = id_tipo_gasto
        self.cantidad = cantidad

    # Representación en cadena
    def __repr__(self) -> str:
        return f'{self.nombre} - ${self.cantidad}'