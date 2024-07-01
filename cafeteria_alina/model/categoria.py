from cafeteria_alina import db

class Categoria(db.Model):
    '''
    Clase que modela una entidad con sus respectivos atributos.

    Entidad: Categoría
    Las categorías sirven para etiquetar productos
    '''

    # Nombre de la tabla
    __tablename__ = 'categoria'
    # PK
    id = db.Column('id', db.Integer, primary_key = True)
    # Nombre de la categoría puesto por el usuario
    nombre = db.Column('nombre', db.String(100), nullable = False)
    # Descripción del producto (opcional)
    descripcion = db.Column('descripcion', db.Text)

    ## Pertenecer
    productos = db.relationship('Producto', back_populates = 'categoria')

    # Constructor
    def __init__(self, 
                 nombre,
                 descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    # Representación en cadena
    def __repr__(self) -> str:
        return f'{self.id}: {self.nombre}'