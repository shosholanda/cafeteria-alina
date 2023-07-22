import datetime
from cafeteria_alina import db


class Insumo(db.Model):
    
    __tablename__ = 'insumo'
    gtin = db.Column('gtin', db.String(20), primary_key = True)
    correo = db.Column('correo', db.ForeginKey('usuario.correo'), nullable = False)
    nombre = db.Column('nombre', db.String(50), nullable = False)
    descripcion = db.Column('descripcion', db.String(128))
    precio = db.Column('precio', db.Float, nullable = False)
    fecha = db.Column('fecha', db.DateTime, default = datetime.datetime.now())


    def __init__(self,
                 gtin,
                 correo,
                 nombre,
                 descripcion,
                 precio):
        self.gtin = gtin
        self.correo = correo
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

    def __repr__(self) -> str:
        return f'gtin: {self.gtin}'