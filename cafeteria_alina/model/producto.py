from entity.__init__ import db

class Producto(db.Model):

    __tablename = 'producto'
    id_producto = db.Column('id_producto', db.Integer, primary_key = True )
    gtin = db.Column('gtin', db.String(50))
    nombre = db.Column('nombre', db.String(100))
    descripcion  = db.Column('descripcion', db.Text)
    precio = db.Column('precio', db.Float)
    tamaño = db.Column('tamaño', db.Integer)
    categoria = db.Column('id_categoria', db.ForeignKey('categoria'), nullable = False)
    status = db.Column('status', db.Boolean)

    # inversion
    # ganancia

    def __init__(self,


    def __repr__(self):
        return f'nombre: {self.gtin}\t${self.precio}'
