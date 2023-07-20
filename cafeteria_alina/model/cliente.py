from model import db

class Cliente(db.Model):

    __tablename__ = 'cliente'
    id_cliente = db.Column('id_cliente', db.Integer, primary_key = True)
    nombre = db.Column('nombre', db.String(50))


    def __init__(self, 
                 nombre):
        self.nombre = nombre



    def __repr__(self) -> str:
        return f'id_cliente: {self.id_cliente}'