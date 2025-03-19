from models.Ingrediente import Ingrediente
from models.Ingredientes_db import Ingrediente as ingrediente

class Base(Ingrediente):
    def __init__(self, nombre: str, precio: float, calorias: int, unidades: float, es_vegetariano: bool, sabor: str):
        super().__init__(nombre, precio, calorias, unidades, es_vegetariano)
        self.__sabor = sabor

    def abastecer(self):
        '''Abastece cinco unidades del ingrediente base'''
        self.unidades += 5.0
        ingrediente.query.filter_by(nombre = self.nombre).update({"unidades": self.unidades})
        ingrediente.commit()
        
    @property
    def sabor(self):
        return self.__sabor
    @sabor.setter
    def sabor(self, nuevo_sabor:str) -> str:
        if isinstance(nuevo_sabor, str) and nuevo_sabor != '':
            self.__sabor = nuevo_sabor
