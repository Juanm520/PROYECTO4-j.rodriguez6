from config.db import db
from config.marshmallow import ma

class Producto(db.Model):
    '''Modelo de Producto en la base de datos.'''
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    precio_publico = db.Column(db.DECIMAL(10, 2), nullable=False)
    ingrediente1 = db.Column(db.String(100), db.ForeignKey('ingrediente.nombre'), nullable=False)
    ingrediente2 = db.Column(db.String(100), db.ForeignKey('ingrediente.nombre'), nullable=False)
    ingrediente3 = db.Column(db.String(100), db.ForeignKey('ingrediente.nombre'), nullable=False)
    tipo_de_producto = db.Column(db.String(50), nullable=False)
    tipo_vaso = db.Column(db.String(50), nullable=True)
    volumen = db.Column(db.Integer, nullable=True)

class ProductoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Producto
        include_fk = True