from flask import Blueprint, render_template

endpoints_blueprint = Blueprint('endpoints', __name__, url_prefix = '/endpoints')
@endpoints_blueprint.route('/')
def login_controller():
    return render_template('endpoints.html')