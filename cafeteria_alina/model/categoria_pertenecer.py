from cafeteria_alina import db

class CategoriaPertenecer(db.Model):

    __tablename__ = 'categoria_pertenecer'
    id = db.Column('id', db.Integer, primary_key = True)
    id_producto = db.Column('id_producto', db.ForeginKey('producto.id_producto'), nullable = False)
    id_categoria = db.Column('id_categoria', db.ForeginKey('categoria.id_categoria'), nullable = False)

    def __init__(self, 
                 id_producto,
                 id_categoria):
        self.id_producto = id_producto
        self.id_categoria = id_categoria



    def __repr__(self) -> str:
        return f'producto {self.id_producto} en {self.id_categoria}'