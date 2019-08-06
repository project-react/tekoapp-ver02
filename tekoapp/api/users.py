from flask_restplus import Namespace, Resource, fields 
from flask import request, jsonify
from tekoapp import models, services

ns = Namespace('users', description='function for users')
_signup_request_req = ns.model(
    'signup_request_req', models.SignupSchema.signup_request_req
    )

_signup_request_res = ns.model(
    'signup_request_res', models.SignupSchema.signup_request_res
    )

_verify_res = ns.model('', model={
    'message': fields.String(required=True, description='verify success or not'),
})

_login_req = ns.model(
    'login_req', models.UserSchema.user_create_req
)

_changepassword_req = ns.model(
    'changepassword_req', 
    {
        'password' : fields.String(required=True, description='your password'),
        'newpassword' : fields.String(required=True, description='new password')
    }
)

_resetpass_req = ns.model(
    'resetpass_req', 
    {
        'username': fields.String(required=True, description='user username'),
        'email' : fields.String(required=True, description='user email')
    }
)

_logingoogle_req = ns.model(
    'logingoogle_req',
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


@ns.route('/register/')
class Register(Resource):
    @ns.expect(_signup_request_req, validate=True)
    def post(self):
        data = request.json or request.args
        return services.users.signup.make_response(**data)

@ns.route('/register/verify/<string:token>')
class Verify(Resource):
    @ns.marshal_with(_verify_res)
    def get(self, token):
        print(token)
        return services.users.signup.verify(token_string=token)

@ns.route('/login/')
class Login(Resource):
    @ns.expect(_login_req, validate=True)
    def post(self):
        data = request.json or request.args
        return services.users.login.make_response(**data)

@ns.route('/maintainLogin/')
class MaintainLogin(Resource):
    @ns.expect(parser_token)
    def get(self):
        token_string = request.headers.get('Authorization')
        return services.users.login.check.maintain(
            token_string=token_string
        )

# @ns.route('/google/login')
# class Login(Resource):
#     @ns.expect(parser_token, _logingoogle_req, validate=True)
#     def post(self):
#         token = request.headers.get('Authorization')
#         data = request.json or request.args
#         return services.google.login.make_response(token=token, email=data['email'])


@ns.route('/logout/')
class Logout(Resource):
    @ns.expect(parser_token)
    def get(self):
        token = request.headers.get('Authorization')
        return services.users.logout.make_response(
            tokenstring=token
        )

@ns.route('/changePassword/')
class Changepassword(Resource):
    @ns.expect(parser_token, _changepassword_req, validate=True)
    def post(self):
        access_token = request.headers.get('Authorization')
        data = request.json or request.args
        return services.users.changepassword.make_response(
            tokenstring=access_token,
            **data
        )

@ns.route('/resetPassword/')
class Resetpassword(Resource):
    @ns.expect(_resetpass_req, validate=True)
    def post(self):
        data = request.json or request.args
        return services.users.resetpassword.make_response(**data)
