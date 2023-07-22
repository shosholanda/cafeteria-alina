from cafeteria_alina import db

class SucursalRegistrar(db.Model):

    __tablename__ = 'sucursal_registrar'
    id = db.Column('id', db.Integer, primary_key = True)
    id_sucursal = db.Column('id_sucursal', db.ForeginKey('sucursal.id_sucursal'), nullable = False)
    correo = db.Column('correo', db.ForeginKey('usuario.correo'), nullable = False)
    
    def __init__(self, 
                 id_sucursal,
                 correo):
        self.id_sucursal = id_sucursal
        self.correo = correo


    def __repr__(self) -> str:
        return f'usuario {self.correo} en {self.id_sucursal}'