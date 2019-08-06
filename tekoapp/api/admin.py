from flask_restplus import Namespace, Resource, fields
from flask import request, jsonify
from tekoapp import services, helpers

ns = Namespace('admin', description='function for Admin')

parser_verify = ns.parser()
parser_verify.add_argument(
    'Authorization',
    type=str,
    help='Bearer Access Token',
    location='headers',
    required=True
)

_edituser_req = ns.model(
    'edituser_req',
    {
        'old_username': fields.String(required=True, description='old username'),
        'new_username': fields.String(required=True, description='username'),
        'new_email': fields.String(required=True, description='email'),
        'is_admin': fields.Boolean(required=True, description='is admin', default=False)
    }
)

_deleteuser_req = ns.model(
    'deleteuser_req',
    {
        'username': fields.String(required=True, description='username'),
        'email': fields.String(required=True, description='email'),
    }
)

_createuser_req = ns.model(
    'createuser_req',
    {
        'username': fields.String(required=True, description='username'),
        'email': fields.String(required=True, description='email'),
        'is_admin': fields.Boolean(required=True, description='is admin', default=False)
    }
)

_lookaccount_req = ns.model(
    'lookaccount_req',
    {
        'username': fields.String(required=True, description='username'),
        'email': fields.String(required=True, description='email'),
        'look_time': fields.Integer(required=True, description='look_time')
    }
)

@ns.route('/getlistuser/')
class Getlistuser(Resource):
    @ns.expect(parser_verify)
    def get(self):
        token = request.headers.get('Authorization')
        return services.admin.getlistuser.get_list_user(token)

@ns.route('/isAdmin/')
class VerifyAdmin(Resource):
    @ns.expect(parser_verify)
    def get(self):
        token = request.headers.get('Authorization')
        return services.admin.verifyadmin.verify_is_admin_by_token(token)

@ns.route('/edituser/')
class EditUser(Resource):
    @ns.expect(parser_verify, _edituser_req)
    def put(token):
        token = request.headers.get('Authorization')
        services.admin.verifyadmin.verify_is_admin_by_token(token)
        data = request.json or request.args
        return services.admin.edituser.edit_user(**data)

@ns.route('/deleteuser/')
class DeleteUser(Resource):
    @ns.expect(parser_verify, _deleteuser_req)
    def delete(self):
        token = request.headers.get('Authorization')
        data = request.json or request.args
        return services.admin.deleteuser.delete_user_by_account_admin(token, **data)

@ns.route('/createuser/')
class CreateUser(Resource):
    @ns.expect(parser_verify, _createuser_req)
    def post(self):
        token = request.headers.get('Authorization')
        services.admin.verifyadmin.verify_is_admin_by_token(token)
        data = request.json or request.args
        return services.admin.createuser.create_user_by_account_admin(**data)

@ns.route('/lookaccount/')
class LookAccount(Resource):
    @ns.expect(parser_verify, _lookaccount_req)
    def put(self):
        token = request.headers.get('Authorization')
        data = request.json or request.args
        return services.admin.lookaccount.look_account_by_admin(
            token=token,
            **data
        )