from cafeteria_alina import db

class Precio(db.Model):

    __tablename__ = 'precio'
    id_producto = db.Column('id_producto', db.ForeignKey('producto.id_producto'), nullable = False, primary_key = True)
    tamaño = db.Column('tamaño', db.String(10), nullable = False, primary_key = True)
    precio = db.Column('precio', db.Float, nullable = False)


    def __init__(self,
                 id_producto,
                 tamaño,
                 precio):
        self.id_producto = id_producto
        self.tamaño = tamaño
        self.precio = precio

    def __repr__(self) -> str:
        return f'nombre: {self.id_producto}\t${self.precio}'
