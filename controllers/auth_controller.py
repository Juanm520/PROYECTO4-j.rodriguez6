from flask import Blueprint, redirect, request, flash, url_for
from flask_login import login_user, logout_user
from models.Usuario_db import Usuario

auth_blueprint = Blueprint('auth', __name__, url_prefix = '/login/auth')
@auth_blueprint.route('/', methods=['POST'])
def auth_controller():
    '''Endpoint para autenticar usuario'''
    usuario = request.form.get('user')
    contrasena = request.form.get('password')
    user = Usuario.query.filter_by(username=usuario).first()

    if user and user.password == contrasena:
        login_user(user)
        return redirect(url_for('login.login_controller'))
    else:
        flash('Contraseña o usuario incorrecto.', 'error')
        return redirect(url_for('login.login_controller'))

logout_blueprint = Blueprint('logout', __name__, url_prefix = '/login/logout')
@logout_blueprint.route('/', methods=['POST'])
def logout_controller():
    '''Endpoint para cerrar sesion'''
    logout_user()
    flash('Usuario deslogueado.', 'exito')
    return redirect(url_for('login.login_controller'))
