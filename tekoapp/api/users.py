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
        'token' : fields.String(required=True, description='user email'),
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

# @ns.route('/register/verify/<string:token>')
# class Verify(Resource):
#     @ns.marshal_with(_verify_res)
#     def get(self, token):
#         message = services.users.signup.verify(token)
#         return message
#
# @ns.route('/login/')
# class Login(Resource):
#     @ns.expect(_login_req, validate=True)
#     def post(self):
#         data = request.json or request.args
#         return services.users.login.check_info_from_login_request(**data)
#
# @ns.route('/google/login')
# class Login(Resource):
#     @ns.expect(parser_token, _logingoogle_req, validate=True)
#     def post(self):
#         token = request.headers.get('Authorization')
#         data = request.json or request.args
#         return services.google.login.make_response(token=token, email=data['email'])
#
# @ns.route('/logout/')
# class Logout(Resource):
#     @ns.expect(parser_token)
#     def get(self):
#         token = request.headers.get('Authorization')
#         return services.users.logout.check_token_from_logout_request(token)
#
# @ns.route('/changePassword/')
# class Changepassword(Resource):
#     @ns.expect(_changepassword_req, validate=True)
#     def post(self):
#         data = request.json or request.args
#         return services.users.changepassword.check_info_and_res(**data)
#
# @ns.route('/resetPassword/')
# class Resetpassword(Resource):
#     @ns.expect(_resetpass_req, validate=True)
#     def post(self):
#         data = request.json or request.args
#         user = services.users.resetpassword.check_info_form_resetpassword_and_res(**data)
#         return user
#
# @ns.route('/maintainLogin/')
# class MaintainLogin(Resource):
#     @ns.expect(parser_token)
#     def get(self):
#         token = request.headers.get('Authorization')
#         return services.users.login.check_maintain_login(token)
