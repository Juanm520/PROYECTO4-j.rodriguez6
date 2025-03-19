from abc import ABC, abstractmethod

class IProducto(ABC):
    @abstractmethod
    def calcular_costo(self) -> float:
        '''Calcula el costo del producto.'''

    @abstractmethod
    def calcular_rentabilidad(self) -> float:
        '''Calcula la rentabilidad del producto.'''
    
    @abstractmethod
    def calcular_calorias(self) -> float:
        '''Calcula la cantidad de calorias del producto.'''
