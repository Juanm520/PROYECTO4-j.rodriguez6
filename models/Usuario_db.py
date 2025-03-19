import uuid
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from config.db import db

class Usuario(db.Model, UserMixin):
    '''Modelo db de Usuario'''
    id = db.Column(db.String(36), primary_key = True, default = lambda: str(uuid.uuid4()))
    username = db.Column(db.String(150), unique = True, nullable = False)
    password = db.Column(db.String(256), nullable = False)
    es_admin = db.Column(db.Boolean, nullable = True)
    es_empleado = db.Column(db.Boolean, nullable = True)

    def set_password(self, password):
            self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    