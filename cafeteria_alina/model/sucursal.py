from cafeteria_alina import db

class Sucursal(db.Model):
    '''
    Clase que modela una entidad con sus respectivos atributos.

    Entidad: Sucursal
    Nos da la información de esta sucursal
    '''

    # Nombre de la tabla
    __tablename__ = 'sucursal'
    # PK
    id_sucursal = db.Column('id_sucursal', db.Integer, primary_key = True)
    # Nombre de la sucursal puesto por el usuario
    nombre = db.Column('nombre', db.String(10))
    # Dirección separada en campos
    calle = db.Column('calle', db.String(30))
    numero = db.Column('numero', db.String(30))
    colonia = db.Column('colonia', db.String(30))
    municipio = db.Column('municipio', db.String(30))
    ciudad = db.Column('ciudad', db.String(30), nullable = False)
    pais = db.Column('pais', db.String(20), nullable = False)
    # Fecha de creación de esta sucursal 
    # AAA
    inaguracion = db.Column('fecha_inaguración', db.Date, nullable = False)
    # Nos dice si sigue estando activo o no el producto. Por omisión está activo
    status = db.Column('status', db.Boolean, nullable = False, default=True)

    ## Registrar
    usuarios = db.relationship('Usuario', back_populates = 'sucursal')
    


    # Constructor
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

    # Representación en cadena
    def __repr__(self) -> str:
        return f'{self.nombre}: {self.calle} {self.numero} | {self.inaguracion}'
    
    def direccion(self) -> str:
        return f'{self.calle} {self.numero}, {self.colonia}, {self.municipio}, {self.ciudad}, {self.pais}.'
