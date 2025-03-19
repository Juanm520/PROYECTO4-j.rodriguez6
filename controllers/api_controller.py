from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from models.Productos_db import Producto, ProductoSchema
from models.Ingredientes_db import Ingrediente, IngredienteSchema
from controllers.heladeria_controller import heladeria_controller

#API: ENDPOINTS
productos_blueprint = Blueprint('productos', __name__, url_prefix = '/productos')
producto_id_blueprint = Blueprint('producto_id', __name__, url_prefix = '/producto_id')
producto_nombre_blueprint = Blueprint('producto_nombre', __name__, url_prefix = '/producto_nombre')
producto_calorias_blueprint = Blueprint('producto_calorias', __name__, url_prefix = '/producto_calorias')
producto_rentabilidad_blueprint = Blueprint('producto_rentabilidad', __name__, url_prefix = '/producto_rentabilidad')
producto_costo_blueprint = Blueprint('producto_costo', __name__, url_prefix = '/producto_costo')
vender_producto_blueprint = Blueprint('vender_producto', __name__, url_prefix = '/vender_producto')
ingredientes_blueprint = Blueprint('ingredientes', __name__, url_prefix = '/ingredientes')
ingrediente_id_blueprint = Blueprint('ingrediente_id', __name__, url_prefix = '/ingrediente_id')
ingrediente_nombre_blueprint = Blueprint('ingrediente_nombre', __name__, url_prefix = '/ingrediente_nombre')
ingrediente_es_sano_blueprint = Blueprint('ingrediente_sano', __name__, url_prefix = '/ingrediente_es_sano')
ingrediente_reabastecer_blueprint = Blueprint('ingrediente_reabastecer', __name__, url_prefix = '/ingrediente_reabastecer')
ingrediente_renovar_blueprint = Blueprint('ingrediente_renovar', __name__, url_prefix = '/ingrediente_renovar')


#Deficiones de los EndPoints:
@productos_blueprint.route('/')
def productos_controller():
    productos = Producto.query.all()
    return jsonify(ProductoSchema().dump(productos, many = True))

@producto_id_blueprint.route('/')
@login_required
def producto_id_controller():
    if current_user.es_admin or current_user.es_empleado:
        if not request.args.get('id'):
            return jsonify({'error': 'debe agregar parametro id'}), 400
        producto_id = request.args.get('id')
        producto = Producto.query.filter_by(id = producto_id).first()
        if not producto:
            return jsonify({'error': 'No existe el producto'}), 404
        return jsonify(ProductoSchema().dump(producto))
    else:
        return jsonify({'error': 'No autorizado'}), 401

@producto_nombre_blueprint.route('/')
@login_required
def producto_nombre_controller():
    if current_user.es_admin or current_user.es_empleado:
        if not request.args.get('nombre'):
            return jsonify({'error': 'debe agregar parametro nombre'}), 400
        producto_nombre = request.args.get('nombre')
        producto = Producto.query.filter_by(nombre = producto_nombre).first()
        if not producto:
            return jsonify({'error': 'No existe el producto'}), 404
        return jsonify(ProductoSchema().dump(producto))
    else:
        return jsonify({'error': 'No autorizado'}), 401

@producto_calorias_blueprint.route('/')
@login_required
def producto_calorias_controller():
    if not request.args.get('id'):
        return jsonify({'error': 'debe agregar parametro id'}), 400
    producto_id = request.args.get('id')
    #Llama en la bd el producto con el id asociado.
    producto_db = Producto.query.filter_by(id = producto_id).first()
    if not producto_db:
        return jsonify({'error': 'No existe el producto'}), 404
    #Compara y filtra con la lista de productos en la instacia heladeria para el uso del metodo.
    productos_instancia = heladeria_controller().productos
    producto = list(filter(lambda producto: producto.nombre == producto_db.nombre, productos_instancia))
    #Crea el retorno del endpoint.
    producto_calorias = {'id': producto_id, 'nombre':producto[0].nombre, 'calorias': producto[0].calcular_calorias()}
    return jsonify(producto_calorias)
    
@producto_rentabilidad_blueprint.route('/')
@login_required
def producto_rentabilidad_controller():
    if current_user.es_admin:
        if not request.args.get('id'):
            return jsonify({'error': 'debe agregar parametro id'}), 400
        producto_id = request.args.get('id')
        #Llama en la bd el producto con el id asociado.
        producto_db = Producto.query.filter_by(id = producto_id).first()
        if not producto_db:
            return jsonify({'error': 'No existe el producto'}), 404
        #Compara y filtra con la lista de productos en la instacia heladeria para el uso del metodo.
        productos_instancia = heladeria_controller().productos
        producto = list(filter(lambda producto: producto.nombre == producto_db.nombre, productos_instancia))
        #Crea el retorno del endpoint.
        producto_rentabilidad = {'id': producto_id, 'nombre':producto[0].nombre, 'rentabilidad': producto[0].calcular_rentabilidad()}
        return jsonify(producto_rentabilidad)
    else:
        return jsonify({'error': 'No autorizado'}), 401

@producto_costo_blueprint.route('/')
@login_required
def producto_costo_controller():
    if current_user.es_admin:
        if not request.args.get('id'):
            return jsonify({'error': 'debe agregar parametro id'}), 400
        producto_id = request.args.get('id')
        #Llama en la bd el producto con el id asociado.
        producto_db = Producto.query.filter_by(id = producto_id).first()
        if not producto_db:
            return jsonify({'error': 'No existe el producto'}), 404
        #Compara y filtra con la lista de productos en la instacia heladeria para el uso del metodo.
        productos_instancia = heladeria_controller().productos
        producto = list(filter(lambda producto: producto.nombre == producto_db.nombre, productos_instancia))
        #Crea el retorno del endpoint.
        producto_costo = {'id': producto_id, 'nombre':producto[0].nombre, 'rentabilidad': producto[0].calcular_costo()}
        return jsonify(producto_costo)
    else:
        return jsonify({'error': 'No autorizado'}), 401

@vender_producto_blueprint.route('/')
@login_required
def vender_producto_controller():
    if not request.args.get('id'):
        return jsonify({'error': 'debe agregar parametro id'}), 400
    producto_id = request.args.get('id')
    #Llama en la bd el producto con el id asociado.
    producto_db = Producto.query.filter_by(id = producto_id).first()
    if not producto_db:
        return jsonify({'error': 'No existe el producto'}), 404
    #Compara y filtra con la lista de productos en la instacia heladeria para el uso del metodo.
    heladeria = heladeria_controller()
    producto = list(filter(lambda producto: producto.nombre == producto_db.nombre, heladeria.productos))
    #Ejecutar metodo.
    try:
        venta = heladeria.vender(producto[0].nombre)
        #Crea el retorno del endpoint.
        return jsonify(ProductoSchema().dump(producto_db), venta)
    except ValueError as error:
        return jsonify({'error': f'{error}'}), 400
        
@ingredientes_blueprint.route('/')
@login_required
def ingredientes_controller():
    if current_user.es_admin or current_user.es_empleado:
        ingredientes = Ingrediente.query.all()
        return jsonify(IngredienteSchema().dump(ingredientes, many = True))
    else:
        return jsonify({'error': 'No autorizado'}), 401

@ingrediente_id_blueprint.route('/')
@login_required
def ingrediente_id_controller():
    if current_user.es_admin or current_user.es_empleado:
        if not request.args.get('id'):
            return jsonify({'error': 'debe agregar parametro id'}), 400
        ingrediente_id = request.args.get('id')
        ingrediente = Ingrediente.query.filter_by(id = ingrediente_id).first()
        if not ingrediente:
            return jsonify({'error': 'No existe el producto'}), 404
        return jsonify(IngredienteSchema().dump(ingrediente))
    else:
        return jsonify({'error': 'No autorizado'}), 401

@ingrediente_nombre_blueprint.route('/')
@login_required
def ingrediente_nombre_controller():
    if current_user.es_admin or current_user.es_empleado:
        if not request.args.get('nombre'):
            return jsonify({'error': 'debe agregar parametro nombre'}), 400
        ingrediente_nombre = request.args.get('nombre')
        ingrediente = Ingrediente.query.filter_by(nombre = ingrediente_nombre).first()
        if not ingrediente:
            return jsonify({'error': 'No existe el producto'}), 404
        return jsonify(IngredienteSchema().dump(ingrediente))
    else:
        return jsonify({'error': 'No autorizado'}), 401

@ingrediente_es_sano_blueprint.route('/')
@login_required
def ingrediente_es_sano_controller():
    if current_user.es_admin or current_user.es_empleado:
        if not request.args.get('id'):
            return jsonify({'error': 'debe agregar parametro id'}), 400
        ingrediente_id = request.args.get('id')
        #Llama en la bd el producto con el id asociado.
        ingrediente_db = Ingrediente.query.filter_by(id = ingrediente_id).first()
        if not ingrediente_db:
            return jsonify({'error': 'No existe el producto'}), 404
        #Compara y filtra con la lista de productos en la instacia heladeria para el uso del metodo.
        ingredientes_instancia = heladeria_controller().ingredientes
        ingrediente = list(filter(lambda ingrediente: ingrediente.nombre == ingrediente_db.nombre, ingredientes_instancia))
        #Crea el retorno del endpoint.
        ingrediente_es_sano = {'id': ingrediente_id, 'nombre':ingrediente[0].nombre, 'es_sano': ingrediente[0].es_sano()}
        return jsonify(ingrediente_es_sano)
    else:
        return jsonify({'error': 'No autorizado'}), 401

@ingrediente_reabastecer_blueprint.route('/')
@login_required
def ingrediente_reabastecer_controller():
    if current_user.es_admin or current_user.es_empleado:
        if not request.args.get('id'):
            return jsonify({'error': 'debe agregar parametro id'}), 400
        ingrediente_id = request.args.get('id')
        #Llama en la bd el producto con el id asociado.
        ingrediente_db = Ingrediente.query.filter_by(id = ingrediente_id).first()
        if not ingrediente_db:
            return jsonify({'error': 'No existe el producto'}), 404
        #Compara y filtra con la lista de productos en la instacia heladeria para el uso del metodo.
        ingredientes_instancia = heladeria_controller().ingredientes
        ingrediente = list(filter(lambda ingrediente: ingrediente.nombre == ingrediente_db.nombre, ingredientes_instancia))
        #Ejecuta el metodo.
        ingrediente[0].abastecer()
        #Crea el retorno del endpoint.
        ingrediente_abastecido = IngredienteSchema().dump(ingrediente_db)
        return jsonify(ingrediente_abastecido)
    else:
        return jsonify({'error': 'No autorizado'}), 401

@ingrediente_renovar_blueprint.route('/')
@login_required
def ingrediente_renovar_controller():
    if current_user.es_admin or current_user.es_empleado:
        if not request.args.get('id'):
            return jsonify({'error': 'debe agregar parametro id'}), 400
        ingrediente_id = request.args.get('id')
        #Llama en la bd el producto con el id asociado.
        ingrediente_db = Ingrediente.query.filter_by(id = ingrediente_id).first()
        if not ingrediente_db:
            return jsonify({'error': 'No existe el producto'}), 404
        #Determina el tipo de producto, si no es complemento no ejecuta la renovacion.
        if ingrediente_db.tipo_de_ingrediente != 'Complemento':
            return jsonify({'error': 'No es posible renovar el ingrediente al ser una Base'}), 404
        #Ejecutar el metodo si es una base.
        ingredientes_instancia = heladeria_controller().ingredientes
        ingrediente = list(filter(lambda ingrediente: ingrediente.nombre == ingrediente_db.nombre, ingredientes_instancia))
        #Ejecuta el metodo.
        ingrediente[0].renovar_inventario()
        #Crea el retorno del endpoint.
        ingrediente_renovado = IngredienteSchema().dump(ingrediente_db)
        return jsonify(ingrediente_renovado)
    else:
        return jsonify({'error': 'No autorizado'}), 401
    