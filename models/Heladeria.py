from models.Base import Base
from models.Ingredientes_db import Ingrediente

class Heladeria():
    def __init__(self, nombre: str, productos: list, ingredientes: list):
        self.__nombre = nombre
        self.__productos = productos
        self.__ingredientes = ingredientes
        self.__ventas_del_dia = 0.0

    def producto_mas_rentable(self) -> str:
        '''Devuelve el producto mas rentable''' 
        productos = self.__productos
        productos.sort(key= lambda x: x.calcular_rentabilidad(), reverse=True)
        return productos[0].nombre

    def vender(self, nombre_producto: str) -> str:
        '''Vende un producto'''
        producto_a_vender = dict
        #Verificar producto en productos
        for producto in self.__productos:
            if producto.nombre.lower() == nombre_producto.lower():
                producto_a_vender = producto
                break
        #Intenta trabajar el producto, si no existe exceptua y retorna False
        try:
                #verifica cantidad ingredientes
            for ingrediente in producto_a_vender.ingredientes:
                if isinstance(ingrediente, Base) and ingrediente.unidades < 1:
                    raise ValueError(f'Oh no! Nos hemos quedado sin {ingrediente.nombre}☹️')
                if ingrediente.unidades < 0.2:
                    raise ValueError(f'Oh no! Nos hemos quedado sin {ingrediente.nombre}☹️')
                #Resta la cantidad de ingredientes del producto.
            for ingrediente in producto_a_vender.ingredientes:
                if isinstance(ingrediente, Base):
                    ingrediente.unidades -= 1.0
                else:
                    ingrediente.unidades -= 0.2
                 #Actualiza los cambios en la base de datos (Comentado para no implicar la base de datos en la prueba).
                Ingrediente.query.filter_by(nombre = ingrediente.nombre).update({"unidades": ingrediente.unidades})
                Ingrediente.commit()
            #Suma a las ventas del dia
            self.__ventas_del_dia += producto_a_vender.precio_publico
            #Retorna que el producto se vendio
            return '¡Vendido!'
        except AttributeError as error:
            raise ValueError('No existe el producto.') from error
    
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre:str) -> str:
        if isinstance(nuevo_nombre, str) and nuevo_nombre != '':
            self.__nombre = nuevo_nombre
    
    @property
    def productos(self):
        return self.__productos
    @productos.setter
    def productos(self, nuevos_productos: list) -> list:
        if isinstance(nuevos_productos, list) and nuevos_productos != '' and len(nuevos_productos) == 4:
            self.__productos = nuevos_productos
    
    @property
    def ingredientes(self):
        return self.__ingredientes
    @ingredientes.setter
    def ingredientes(self, nuevos_ingredientes: list) -> list:
        if isinstance(nuevos_ingredientes, list):
            self.__ingredientes = nuevos_ingredientes

    @property
    def ventas_del_dia(self):
        return self.__ventas_del_dia
