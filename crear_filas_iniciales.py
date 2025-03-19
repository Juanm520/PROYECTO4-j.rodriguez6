from models.Productos_db import Producto
from models.Ingredientes_db import Ingrediente
from models.Complemento import Complemento
from models.Base import Base
from models.Copa import Copa
from models.Malteada import Malteada
from models.Usuario_db import Usuario

def crear_filas(db):
    if db.session.query(Ingrediente).count() == 0:
            #Bases
        helado_fresa = Base('Helado de Fresa', 1200, 26, 1, False, 'Fresa')
        helado_chocolate = Base('Helado de Chocolate', 1900, 40, 10, False, 'Chocolate')
        helado_mandarina = Base('Helado de Mandarina', 1200, 40, 0, False, 'Mandarina')
        fruta_congelada = Base('Mix Frutas Congeladas', 1450, 120, 10, True, 'Banano, Kiwi y Fresa')
                #Complementos
        chispas_chocolate = Complemento('Chispas de chocolate', 500, 20, 5, False)
        mani = Complemento('Mani', 900, 35, 5, True)
        salsa_mora = Complemento('Salsa de Mora', 300, 40, 5, True)
        masmelo = Complemento('Masmelo', 500, 110, 10, False)

            #Productos
                #Ingredientes de los prodcutos
        ingredientes_copa_junior = [helado_fresa, chispas_chocolate, mani]
        ingredientes_copa_chocolate = [helado_chocolate, fruta_congelada, masmelo]
        ingredientes_malteada_mandarina = [helado_mandarina, mani, chispas_chocolate] 
        ingredientes_malteada_fresa = [helado_fresa, salsa_mora, chispas_chocolate] 
                #Copas
        copa_junior = Copa('Copa Junior', 12000, ingredientes_copa_junior, "mediano")
        copa_chocolate = Copa('Copa Chocolate', 18000, ingredientes_copa_chocolate, "grande")
        malteada_mandarina = Malteada('Malteada de Mandarina', 18000, ingredientes_malteada_mandarina, 13)
        malteada_fresa = Malteada('Malteada de Fresa', 18000, ingredientes_malteada_fresa, 13)

        ingredientes = [helado_fresa, helado_chocolate,  helado_mandarina, fruta_congelada, chispas_chocolate, mani, salsa_mora, masmelo]
        productos = [copa_junior, copa_chocolate, malteada_mandarina, malteada_fresa]


            #Creando filas de la tabla ingredientes.
        ingredientes_a_agregar = []

        for ingrediente in ingredientes:
            if isinstance(ingrediente, Base):
                ingredientes_a_agregar.append(Ingrediente(nombre = ingrediente.nombre,
                                                precio = ingrediente.precio,
                                                calorias = ingrediente.calorias,
                                                unidades = ingrediente.unidades,
                                                es_vegetariano = ingrediente.es_vegetariano,
                                                tipo_de_ingrediente = 'Base',
                                                sabor = ingrediente.sabor))
            else:    
                ingredientes_a_agregar.append(Ingrediente(nombre = ingrediente.nombre,
                                                precio = ingrediente.precio,
                                                calorias = ingrediente.calorias,
                                                unidades = ingrediente.unidades,
                                                es_vegetariano = ingrediente.es_vegetariano,
                                                tipo_de_ingrediente = 'Complemento'))

            #Creando filas de la tabla productos.
        productos_a_agregar = []

        for producto in productos:
            if isinstance(producto, Copa):
                productos_a_agregar.append(Producto(nombre = producto.nombre, 
                            precio_publico = producto.precio_publico, 
                            ingrediente1 = producto.ingredientes[0].nombre,
                            ingrediente2 = producto.ingredientes[1].nombre,
                            ingrediente3 = producto.ingredientes[2].nombre,
                            tipo_de_producto = 'Copa', 
                            tipo_vaso = producto.tipo_vaso
                            ))
            else:   
                    productos_a_agregar.append(Producto(nombre = producto.nombre,
                            precio_publico = producto.precio_publico,
                            ingrediente1 = producto.ingredientes[0].nombre, 
                            ingrediente2 = producto.ingredientes[1].nombre, 
                            ingrediente3 = producto.ingredientes[2].nombre, 
                            tipo_de_producto = 'Malteada',
                            volumen = producto.volumen))

        #usuarios
        usuarios_a_agregar = []
        usuarios_a_agregar.append(Usuario(username = 'admin',
                                          password = 'admin1',
                                          es_admin = True,
                                          es_empleado = False))
        usuarios_a_agregar.append(Usuario(username = 'empleado',
                                          password = 'empleado1',
                                          es_admin = False,
                                          es_empleado = True))
        usuarios_a_agregar.append(Usuario(username = 'cliente',
                                          password = 'cliente1',
                                          es_admin = False,
                                          es_empleado = False))

        db.session.add_all(ingredientes_a_agregar)
        db.session.add_all(productos_a_agregar)
        db.session.add_all(usuarios_a_agregar)
        db.session.commit()
    else:
         print('>>Datos iniciales ya agregados en la base de datos.')
    
    if db.session.query(Usuario).count() == 0:
    #usuarios
        usuarios_a_agregar = []
        usuarios_a_agregar.append(Usuario(username = 'admin',
                                          password = 'admin1',
                                          es_admin = True,
                                          es_empleado = False))
        usuarios_a_agregar.append(Usuario(username = 'empleado',
                                          password = 'empleado1',
                                          es_admin = False,
                                          es_empleado = True))
        usuarios_a_agregar.append(Usuario(username = 'cliente',
                                          password = 'cliente1',
                                          es_admin = False,
                                          es_empleado = False))

        db.session.add_all(usuarios_a_agregar)
        db.session.commit()
    else:
        print('>>Usuarios ya agregados en la base de datos.')
