import json
from tekoapp import repositories as r
from tekoapp.tests.api import APITestCase
from . import mock


class VerifyAdminApiTestCase(APITestCase):
    def url(self):
        return 'http://127.0.0.1:5000/api/admin/isAdmin/'

    def method(self):
        return 'GET'

    def test_verify_admin(self):
        user = mock.account_is_admin()
        user_token = r.usertoken.add.by_user_model(
            user=user['info']
        )
        headers = {
            'Authorization': user_token.token
        }
        res = self.send_request(headers=headers)
        self.assertEqual(200, res.status_code)
        self.assertEqual(True, json.loads(res.data))


class GetListUserApiTestCase(APITestCase):
    def url(self):
        return 'http://127.0.0.1:5000/api/admin/getListUser/'

    def method(self):
        return 'GET'

    def test_get_list_user(self):
        user = mock.account_is_admin()
        user_token = r.usertoken.add.by_user_model(
            user=user['info']
        )
        headers = {
            'Authorization': user_token.token
        }
        res = self.send_request(headers=headers)
        print(json.loads(res.data))
        print(len(json.loads(res.data)))
        self.assertEqual(200, res.status_code)
        self.assertEqual(1, len(json.loads(res.data)))


class EditUserApiTestCase(APITestCase):
    def url(self):
        return 'http://127.0.0.1:5000/api/admin/editUser/'

    def method(self):
        return 'PUT'

    def test_edit_user(self):
        admin = mock.account_is_admin()
        user_token = r.usertoken.add.by_user_model(
            user=admin['info']
        )
        user_edit = mock.account_is_user()
        headers = {
            'Authorization': user_token.token
        }
        data = {
            "user_edited_id": user_edit['info'].id,
            "new_username": "chiennguyen1999",
            "new_email": "duychien226@gmail.com",
            "new_is_admin": True,
        }
        res = self.send_request(data=data, headers=headers)
        print(len(json.loads(res.data)))
        self.assertEqual(200, res.status_code)
        check_user_edit = r.user.find.by_email_or_username(
            username="chiennguyen1999",
            email="duychien226@gmail.com"
        )
        assert check_user_edit


class CreateUserApiTestCase(APITestCase):
    def url(self):
        return 'http://127.0.0.1:5000/api/admin/createUser/'

    def method(self):
        return 'POST'

    def test_create_user(self):
        admin = mock.account_is_admin()
        user_token = r.usertoken.add.by_user_model(
            user=admin['info']
        )
        headers = {
            'Authorization': user_token.token
        }
        data = {
            "username": "chiennguyen99",
            "email": "duychien26@gmail.com",
            "is_admin": True
        }
        res = self.send_request(data=data, headers=headers)
        self.assertEqual(200, res.status_code)


class LookAccountApiTestCase(APITestCase):
    def url(self):
        return 'http://127.0.0.1:5000/api/admin/lookAccount/'

    def method(self):
        return 'PUT'

    def test_lock_account(self):
        admin = mock.account_is_admin()
        user_token = r.usertoken.add.by_user_model(
            user=admin['info']
        )
        headers = {
            'Authorization': user_token.token
        }
        user = mock.account_is_user()
        data = {
            "user_id": user['info'].id,
            "lock_time": 1,
        }
        res = self.send_request(data=data, headers=headers)
        self.assertEqual(200, res.status_code)


class DeleteUserApiTestCase(APITestCase):
    def url(self):
        return 'http://127.0.0.1:5000/api/admin/deleteUser/'

    def method(self):
        return 'DELETE'

    def test_delete_account(self):
        admin = mock.account_is_admin()
        user_token = r.usertoken.add.by_user_model(
            user=admin['info']
        )
        headers = {
            'Authorization': user_token.token
        }
        user = mock.account_is_user()
        data = {
            "user_id": user['info'].id,
        }
        res = self.send_request(data=data, headers=headers)
        self.assertEqual(200, res.status_code)



