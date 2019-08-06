from flask import Blueprint
from flask_restplus import Api
from .users import ns as users_ns
from .admin import ns as admin_ns

api_bp = Blueprint('api', __name__, url_prefix='/api')

api = Api(
    app=api_bp,
    version='1.0',
    title='API',
    validate=False,
)

def init_app(app, **kwargs):
    """
    :param flask.Flask app: the app
    :param kwargs:
    :return:
    """
    api.add_namespace(users_ns)
    api.add_namespace(admin_ns)
    app.register_blueprint(api_bp)