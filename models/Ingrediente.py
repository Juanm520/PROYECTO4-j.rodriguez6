from abc import ABC, abstractmethod

class Ingrediente(ABC):
    def __init__(self, nombre: str, precio: float, calorias: int, unidades: float, es_vegetariano: bool):
        self.__nombre = nombre
        self.__precio = precio
        self.__calorias = calorias
        self.__unidades = unidades
        self.__es_vegetariano = es_vegetariano

    def es_sano(self) -> bool:
        '''Define si el ingrediente es sano.'''
        if self.__es_vegetariano or self.__calorias < 100:
            return True
        return False
    
    @abstractmethod
    def abastecer(self):
        '''Agrega unidades del ingrediente'''
    
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre:str) -> str:
        if isinstance(nuevo_nombre, str) and nuevo_nombre != '':
            self.__nombre = nuevo_nombre

    @property
    def precio(self):
        return self.__precio
    @precio.setter
    def precio(self, nuevo_precio:float) -> float:
        if isinstance(nuevo_precio, float) and nuevo_precio != '':
            self.__precio = nuevo_precio
    
    @property
    def calorias(self):
        return self.__calorias
    @calorias.setter
    def calorias(self, nuevas_calorias:int) -> int:
        if isinstance(nuevas_calorias, int) and nuevas_calorias != '':
            self.__calorias = nuevas_calorias

    @property
    def unidades(self):
        return self.__unidades
    @unidades.setter
    def unidades(self, nuevas_unidades: float) -> float:
        if isinstance(nuevas_unidades, float) and nuevas_unidades != '':
            self.__unidades = nuevas_unidades
   
    @property
    def es_vegetariano(self):
        return self.__es_vegetariano
    @es_vegetariano.setter
    def es_vegetariano(self, nuevo_parametro: bool) -> bool:
        if isinstance(nuevo_parametro, bool) and nuevo_parametro != '':
            self.__es_vegetariano = nuevo_parametro
