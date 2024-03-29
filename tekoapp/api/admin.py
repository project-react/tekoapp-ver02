from flask_restplus import Namespace, Resource, fields
from flask import request
from tekoapp import services

ns = Namespace('admin', description='function for admin')

parser_verify = ns.parser()
parser_verify.add_argument(
    'Authorization',
    type=str,
    help='Bearer Access Token',
    location='headers',
    required=True
)

_edit_user_req = ns.model(
    'edit_user_req',
    {
        'user_edited_id': fields.Integer(required=True),
        'new_username': fields.String(required=True),
        'new_email': fields.String(required=True),
        'new_is_admin': fields.Boolean(required=True, default=False)
    }
)

_delete_user_req = ns.model(
    'delete_user_req',
    {
        'user_id': fields.Integer(required=True)
    }
)

_create_user_req = ns.model(
    'create_user_req',
    {
        'username': fields.String(required=True),
        'email': fields.String(required=True),
        'is_admin': fields.Boolean(required=True, default=False)
    }
)

_lock_account_req = ns.model(
    'lock_account_req',
    {
        'user_id': fields.Integer(required=True),
        'lock_time': fields.Integer(required=True),
    }
)


@ns.route('/getListUser/')
class GetListUser(Resource):
    @ns.expect(parser_verify)
    def get(self):
        token = request.headers.get('Authorization')
        return services.admin.getlistuser.make_response(
            token=token
        )


@ns.route('/isAdmin/')
class VerifyAdmin(Resource):
    @ns.expect(parser_verify)
    def get(self):
        token = request.headers.get('Authorization')
        return services.admin.verifyadmin.make_response(
            token=token
        )


@ns.route('/editUser/')
class EditUser(Resource):
    @ns.expect(parser_verify, _edit_user_req)
    def put(self):
        token = request.headers.get('Authorization')
        services.admin.verifyadmin.make_response(token=token)
        data = request.json or request.args
        return services.admin.edituser.make_response(**data)


@ns.route('/deleteUser/')
class DeleteUser(Resource):
    @ns.expect(parser_verify, _delete_user_req)
    def delete(self):
        token = request.headers.get('Authorization')
        data = request.json or request.args
        return services.admin.deleteuser.make_response(token=token, **data)


@ns.route('/createUser/')
class CreateUser(Resource):
    @ns.expect(parser_verify, _create_user_req)
    def post(self):
        token = request.headers.get('Authorization')
        services.admin.verifyadmin.make_response(token=token)
        data = request.json or request.args
        return services.admin.createuser.make_response(**data)


@ns.route('/lookAccount/')
class LookAccount(Resource):
    @ns.expect(parser_verify, _lock_account_req)
    def put(self):
        token = request.headers.get('Authorization')
        data = request.json or request.args
        return services.admin.lookaccount.make_response(
            token=token,
            **data
        )

