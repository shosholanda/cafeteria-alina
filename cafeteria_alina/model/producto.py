from cafeteria_alina import db

class Producto(db.Model):

    __tablename = 'producto'
    id_producto = db.Column('id_producto', db.Integer, primary_key = True )
    nombre = db.Column('nombre', db.String(100), nullable = False)
    descripcion  = db.Column('descripcion', db.Text)
    tamaño = db.Column('tamaño', db.String(10))
    precio = db.Column('precio', db.Float, nullable = False)
    status = db.Column('status', db.Boolean, default = True)

    # inversion
    # ganancia

    def __init__(self,
                 id_producto,
                 nombre,
                 descripcion,
                 tamaño,
                 precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.tamaño = tamaño
        self.precio = precio

    def __repr__(self) -> str:
        return f'nombre: {self.id_producto}\t${self.precio}'
