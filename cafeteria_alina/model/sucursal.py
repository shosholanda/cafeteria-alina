from cafeteria_alina import db

class Sucursal(db.Model):

    __tablename__ = 'sucursal'
    id_sucursal = db.Column('id_sucursal', db.Integer, primary_key = True)
    nombre = db.Column('nombre', db.String(10))
    inaguracion = db.Column('fecha_inaguración', db.Date, nullable = False)
    pais = db.Column('pais', db.String(20), nullable = False)
    ciudad = db.Column('ciudad', db.String(30), nullable = False)
    municipio = db.Column('municipio', db.String(30))
    calle = db.Column('calle', db.String(30))
    colonia = db.Column('colonia', db.String(30))
    numero = db.Column('numero', db.String(30))

    def __init__(self,
                 nombre,
                 inaguracion, 
                 pais, 
                 ciudad, 
                 municipio,
                 calle,
                 colonia,
                 numero):
        self.nombre = nombre
        self.inaguracion = inaguracion
        self.pais = pais
        self.ciudad = ciudad
        self.municipio = municipio
        self.calle = calle
        self.colonia = colonia
        self.numero = numero

    
    def __repr__(self) -> str:
        return f'{self.nombre}: {self.calle} {self.numero}, {self.colonia}, {self.municipio}, {self.ciudad} {self.pais}'
