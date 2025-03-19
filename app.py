from flask import Flask, jsonify
from flask_login import LoginManager
from config.config import Config
from config.db import db
from config.marshmallow import ma
from config.routes import register_routes
from models.Usuario_db import Usuario
from crear_filas_iniciales import crear_filas

app = Flask(__name__, template_folder='views')
application = app
app.config.from_object(Config)
login_manager = LoginManager(app)
db.init_app(app)
ma.init_app(app)
register_routes(app)

@login_manager.user_loader
def load_user(user: int):
    '''Carga el usuario en el login_manager'''
    return Usuario.query.get(user)

@login_manager.unauthorized_handler
def no_autenticado():
    return jsonify({"error": 'No autorizado'}), 401

with app.app_context():
    db.create_all()
    crear_filas(db)

if __name__ == '__main__':
    app.run(debug=True)
