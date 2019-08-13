import json
from tekoapp.tests.api import APITestCase
from tekoapp import repositories as r
from . import mock


class SignUpApiTestCase(APITestCase):
    def url(self):
        return 'http://127.0.0.1:5000/api/users/register/'

    def method(self):
        return 'POST'

    def test_signup(self):
        data = {
            'email': 'besora@getvmail.net',
            'username': 'chiennguyen99',
            'password': 'Nguyenduychien1.',
        }
        res = self.send_request(data=data)
        self.assertEqual(200, res.status_code)
        check_data_exist = r.signup.find.by_email_or_username(
            email='besora@getvmail.net',
            username='chiennguyen99'
        )
        assert check_data_exist
        self.assertEqual(
            check_data_exist.username, 'chiennguyen99'
        )
        self.assertEqual(
            check_data_exist.email, 'besora@getvmail.net'
        )

    def test_status_res(self):
        array_input = [
            {
                'username': 'chien',
                'email': 'besoa@getvmail.net',
                'password': 'Nguyenduychien',
                'status_code': 400
            },
            {
                'username': 'nguyenduychien',
                'email': 'beso@getvmail,net',
                'password': 'Nguyenduychien1.',
                'status_code': 400
            },
            {
                'username': 'nguyenduyc/',
                'email': 'beso@getvmail.net',
                'password': 'Nguyenduychien1."',
                'status_code': 400
            },
            {
                'username': '123456789',
                'email': '@gmail.com',
                'password': 'Nguyenduychien1.',
                'status_code': 400
            },
            {
                'username': 'nguyenduychien',
                'email': 'besora@getvmail.net',
                'password': 'Nguyenduychien1.',
                'status_code': 200
            },
        ]
        results = []
        for input in array_input:
            data = {
                'email': input['email'],
                'username': input['username'],
                'password': input['password'],
            }
            res = self.send_request(data=data)
            results.append(input["status_code"] == res.status_code)
        i = 1
        flag = True
        for result in results:
            if result == False:
                print("data test register error index: " + str(i))
                flag = False
            i += 1
        if flag:
            self.assertEqual(True, True)
        else:
            self.assertEqual(True, False)


class LoginApiTestCase(APITestCase):
    def url(self):
        return 'http://127.0.0.1:5000/api/users/login/'

    def method(self):
        return 'POST'

    def test_login(self):
        user = mock.account_is_user()
        user_test = r.user.find.by_email_or_username(
            username=user['info'].username,
            email=user['info'].email,
        )
        assert user_test
        self.assertEqual(user['info'].username, 'chiennguyen99')
        valid_data = {
            'username': user['info'].username,
            'password': user['password']
        }
        res = self.send_request(data=valid_data)
        check_exist_user_token = r.usertoken.find.by_user_id(
            user_id=user['info'].id,
        )
        assert check_exist_user_token
        self.assertEqual(200, res.status_code)

    def test_status_res(self):
        input = [
            {
                'data': {
                    'username': 'Chiennguyen99',
                    'password': 'Nguyenduychien1.',
                },
                'status': 401,
                'msg': 'Not found user',
            },
            {
                'data': {
                    'username': 'Chien123.',
                    'password': '123',
                },
                'status': 400,
                'msg': 'Data invalid!',
            },
            {
                'data': {
                    'username': 'Chien123.',
                    'password': '123',
                },
                'status': 400,
                'msg': 'Data invalid!',
            }
        ]
        for value in input:
            res = self.send_request(data=value['data'])
            print(json.loads(res.data)['message'])
            self.assertEqual(value['status'], res.status_code)
            self.assertEqual(value['msg'], json.loads(res.data)['message'])


class ResetPasswordApiTestCase(APITestCase):
    def url(self):
        return 'http://127.0.0.1:5000/api/users/resetPassword/'

    def method(self):
        return 'POST'

    def test_reset_password(self):
        user = mock.account_is_user()
        valid_data = {
            'username': user['info'].username,
            'email': user['info'].email,
        }
        res = self.send_request(data=valid_data)
        self.assertEqual(200, res.status_code)

    def test_status_res(self):
        inputs=[
            {
                'data': {
                    'username': '123',
                    'email': '123',
                },
                'status': 400,
                'msg': 'Data invalid!',
            },
            {
                'data': {
                    'username': '123',
                    'email': 'duychien226@gmail.com',
                },
                'status': 400,
                'msg': 'Data invalid!',
            },
            {
                'data': {
                    'username': 'chiennguyen99',
                    'email': '123',
                },
                'status': 400,
                'msg': 'Data invalid!',
            },
            {
                'data': {
                    'username': 'chiennguyen99',
                    'email': 'duychien226@gmail.com',
                },
                'status': 400,
                'msg': 'account not exist!',
            },
        ]
        for input in inputs:
            res = self.send_request(data=input['data'])
            print(json.loads(res.data)['message'])
            self.assertEqual(input['status'], res.status_code)
            self.assertEqual(input['msg'], json.loads(res.data)['message'])


class ChangePasswordApiTestCase(APITestCase):
    def url(self):
        return 'http://127.0.0.1:5000/api/users/changePassword/'

    def method(self):
        return 'POST'

    def test_change_password(self):
        user = mock.account_is_user()
        user_token = r.usertoken.add.by_user_model(
            user=user['info']
        )
        headers = {
            'Authorization': user_token.token
        }
        valid_data = {
            'password': user['password'],
            'new_password': 'Nguyenduychien1.',
        }
        res = self.send_request(data=valid_data, headers=headers)
        self.assertEqual(200, res.status_code)


class LogoutApiTestCase(APITestCase):
    def url(self):
        return 'http://127.0.0.1:5000/api/users/logout/'

    def method(self):
        return 'GET'

    def test_logout(self):
        user = mock.account_is_user()
        user_token = r.usertoken.add.by_user_model(
            user=user['info']
        )
        headers = {
            'Authorization': user_token.token
        }
        self.send_request(headers=headers)
        find_user_token_test = r.usertoken.find.by_access_token(
            access_token=user_token.token
        )
        self.assertEqual(find_user_token_test, None)






