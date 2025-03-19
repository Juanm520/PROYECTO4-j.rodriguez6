from models.Ingrediente import Ingrediente
from models.Ingredientes_db import Ingrediente as ingrediente

class Complemento(Ingrediente):
    def __init__(self, nombre: str, precio: float, calorias: int, unidades: float, es_vegetariano: bool):
        super().__init__(nombre, precio, calorias, unidades, es_vegetariano)
       
    def abastecer(self):
        '''Abastece diez unidades del ingrediente base.'''
        self.unidades += 10.0
        ingrediente.query.filter_by(nombre = self.nombre).update({"unidades": self.unidades})
        ingrediente.commit()
       
    def renovar_inventario(self):
        '''Devuelve a cero las unidades del ingrediente.'''
        self.unidades = 0.0
        ingrediente.query.filter_by(nombre = self.nombre).update({"unidades": 0.0})
        ingrediente.commit()
