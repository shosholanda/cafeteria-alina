from cafeteria_alina import db

class Producto(db.Model):

    __tablename__ = 'producto'
    id_producto = db.Column('id_producto', db.String(100), primary_key = True )
    nombre = db.Column('nombre', db.String(100), nullable = False)
    descripcion  = db.Column('descripcion', db.Text, default = 'Sin descripcion')
    status = db.Column('status', db.Boolean, nullable = False, default=True)


    def __init__(self,
                 id_producto,
                 nombre,
                 descripcion):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion

    def __repr__(self) -> str:
        return f'nombre: {self.nombre}'
