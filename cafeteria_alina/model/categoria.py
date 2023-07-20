from model import db


class Categoria(db.Model):

    __tablename__ = 'categoria'
    id_categoria = db.Column('id_categoria', db.Integer, primary_key = True)
    nombre = db.Column('nombre', db.String(20), nullable = False)
    descripcion = db.Column('descripcion', db.Text)


    def __init__(self, 
                 nombre,
                 descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def __repr__(self) -> str:
        return f'nombre: {self.nombre}'