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

_change_password_req = ns.model(
    'change_password_req',
    {
        'password': fields.String(required=True),
        'new_password': fields.String(required=True)
    }
)

_reset_pass_req = ns.model(
    'reset_pass_req',
    {
        'username': fields.String(required=True, description='user username'),
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
        return services.users.signup.verify(access_token=token)


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
            access_token=token_string
        )


@ns.route('/logout/')
class Logout(Resource):
    @ns.expect(parser_token)
    def get(self):
        token = request.headers.get('Authorization')
        return services.users.logout.make_response(
            access_token=token
        )


@ns.route('/changePassword/')
class ChangePassword(Resource):
    @ns.expect(parser_token, _change_password_req, validate=True)
    def post(self):
        access_token = request.headers.get('Authorization')
        data = request.json or request.args
        return services.users.changepassword.make_response(
            access_token=access_token,
            **data
        )


@ns.route('/resetPassword/')
class ResetPassword(Resource):
    @ns.expect(_reset_pass_req, validate=True)
    def post(self):
        data = request.json or request.args
        return services.users.resetpassword.make_response(**data)
