from cafeteria_alina import db

class Insumo(db.Model):
    '''
    Clase que modela una entidad con sus respectivos atributos.

    Entidad: Insumo
    Nos da los productos que se inverten para generar otros productos.
    '''

    # Nombre de la tabla
    __tablename__ = 'insumo'
    # PK
    gtin = db.Column('gtin', db.Integer, primary_key = True)
    # Nombre del insumo puesto por el usuario
    nombre = db.Column('nombre', db.String(50), nullable = False)
    # Precio del insumo.
    precio = db.Column('precio', db.Float, nullable = False)
    # Descripción del insumo (opcional)
    descripcion = db.Column('descripcion', db.String(128))


    # Constructor
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

    # Representación en cadena
    def __repr__(self) -> str:
        return f'{self.nombre} - ${self.precio}'