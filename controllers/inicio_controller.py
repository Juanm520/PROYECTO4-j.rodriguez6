from flask import Blueprint, render_template
from models.Productos_db import Producto

inicio_blueprint = Blueprint('inicio', __name__, url_prefix = '/')

@inicio_blueprint.route('/')
def inicio_controller():
    productos = Producto.query.all()
    return render_template('index.html', productos = productos)
