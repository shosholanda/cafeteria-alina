from cafeteria_alina import db

class Producto(db.Model):

    __tablename__ = 'producto'
    id_producto = db.Column('id_producto', db.Integer, primary_key = True )
    nombre = db.Column('nombre', db.String(100), nullable = False)
    descripcion  = db.Column('descripcion', db.Text)
    status = db.Column('status', db.Boolean, nullable = False, default=True)

    # inversion
    # ganancia

    def __init__(self,
                 id_producto,
                 nombre,
                 descripcion):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion

    def __repr__(self) -> str:
        return f'nombre: {self.nombre}'
