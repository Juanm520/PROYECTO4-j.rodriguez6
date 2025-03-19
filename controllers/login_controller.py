from flask import Blueprint, render_template

login_blueprint = Blueprint('login', __name__, url_prefix = '/login')
@login_blueprint.route('/')
def login_controller():
    return render_template('login.html')

