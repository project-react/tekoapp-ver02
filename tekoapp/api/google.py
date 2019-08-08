from flask_restplus import Namespace, Resource, fields
from flask import request
from tekoapp import services


ns = Namespace('google', description='function for google')

_login_google_req = ns.model(
    'login_google_req',
    {
        'email': fields.String(required=True, description='user email')
    }
)

parser_token = ns.parser()
parser_token.add_argument(
    'Authorization',
    type=str,
    help='Bearer Access Token',
    location='headers',
    required=True
)


@ns.route('/login/')
class LoginGoogle(Resource):
    @ns.expect(parser_token, _login_google_req, validate=True)
    def post(self):
        token = request.headers.get('Authorization')
        data = request.json or request.args
        return services.google.login.make_response(token=token, email=data['email'])

