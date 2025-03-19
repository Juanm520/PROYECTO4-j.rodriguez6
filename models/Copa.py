from models.IProducto import IProducto

class Copa(IProducto):
    def __init__(self, nombre: str, precio_publico: float, ingredientes: list, tipo_vaso: str):
        self.__nombre = nombre
        self.__precio_publico = precio_publico
        self.__ingredientes = ingredientes
        self.__tipo_vaso = tipo_vaso

    def calcular_costo(self) -> float:
        '''Calcula el costo del producto.'''
        costo = 0.0
        for ingrediente in self.__ingredientes:
            costo += ingrediente.precio
        return costo
       
    def calcular_rentabilidad(self) -> float:
        '''Calcula la rentabilidad del producto.'''
        costo_total = self.calcular_costo()
        return self.__precio_publico - costo_total
    
    def calcular_calorias(self) -> float:
        '''Calcula la cantidad de calorias del producto.'''
        calorias_totales = 0.0
        for ingrediente in self.__ingredientes:
            calorias_totales += ingrediente.calorias
        return round(calorias_totales * 0.95, 2)

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre:str) -> str:
        if isinstance(nuevo_nombre, str) and nuevo_nombre != '':
            self.__nombre = nuevo_nombre

    @property
    def precio_publico(self):
        return self.__precio_publico
    @precio_publico.setter
    def precio_publico(self, nuevo_precio:float) -> float:
        if isinstance(nuevo_precio, float) and nuevo_precio != '':
            self.__precio_publico = nuevo_precio
    
    @property
    def ingredientes(self):
        return self.__ingredientes
    @ingredientes.setter
    def ingredientes(self, nuevos_ingredientes:list) -> list:
        if isinstance(nuevos_ingredientes, list) and nuevos_ingredientes != '' and len(nuevos_ingredientes) == 3:
            self.__ingredientes = nuevos_ingredientes
    
    @property
    def tipo_vaso(self):
        return self.__tipo_vaso
    @tipo_vaso.setter
    def tipo_vaso(self, nuevo_tipo_vaso:str) -> str:
        if isinstance(nuevo_tipo_vaso, str) and nuevo_tipo_vaso != '':
            self.__tipo_vaso = nuevo_tipo_vaso
