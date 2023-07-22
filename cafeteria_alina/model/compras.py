from cafeteria_alina import db
import datetime

class Compras(db.Model):

    __tablename__ = 'compras'
    id_compra = db.Column('id_compra', db.Integer, primary_key = True)
    id_producto = db.Column('id_producto', db.ForeginKey('producto.id_producto'), nullable = False)
    correo = db.Column('correo', db.ForeginKey('usuario.correo'), nullable = False)
    id_cliente = db.Column('id_cliente', db.ForeginKey('cliente.id_cliente'), nullable = False)
    cantidad = db.Column('cantidad', db.Integer, unsigned = True, default = 1)
    fecha = db.Column('fecha', db.DateTime, default = datetime.datetime.now())
    deuda = db.Column('deuda', db.Float, default = 0.0)

    def __init__(self, 
                 id_producto,
                 correo,
                 id_cliente,
                 cantidad,
                 deuda):
        self.id_producto = id_producto
        self.correo = correo
        self.id_cliente = id_cliente
        self.cantidad = cantidad
        self.deuda = deuda



    def __repr__(self) -> str:
        return f'compra:{self.cantidad} {self.id_producto} por {self.correo}'