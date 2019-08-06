import json
import logging
import jwt
import config
import re

from datetime import datetime, timedelta
from tekoapp import models as m
from tekoapp.tests.api import APITestCase
from tekoapp import repositories as r, helpers

_logger = logging.getLogger(__name__)

email = 'fofef@simplemail.in'

data_test_register = \
    '[ ' \
         '{"username": "chien", "email": "duychien22@gmail.com", "password": "Nguyenduychien", "status_code": 400}, ' \
         '{"username": "nguyenduychien", "email": "duychien22gmail.com", "password": "Nguyenduychien1.", "status_code": 400}, ' \
         '{"username": "nguyenduyc/", "email": "duychien22@gmail.com", "password": "Nguyenduychien1.", "status_code": 400}, ' \
         '{"username": "123456789", "email": "@gmail.com", "password": "Nguyenduychien1.", "status_code": 400}, ' \
         '{"username": "444444444", "email": "duychien22@.", "password": "Nguyenduychien1.", "status_code": 400}, ' \
         '{"username": "", "email": "duychien22@gmail.com", "password": "Nguyenduychien1.", "status_code": 400}, ' \
         '{"username": "", "email": "", "password": "", "status_code": 400},' \
         '{"username": "nguyenduychien", "email": "duychien226@gmail.com", "password": "Nguyenduychien1.", "status_code": 200}]'



def create_mock_user():
    global email
    mock_data = {
        'username': 'nguyenduychien',
        'email': email,
        'password': 'Nguyenduychien1.',
    }
    signup_req = r.signup.save_user_to_signup_request(
        **mock_data
    )
    user = r.signup.save_user_to_user(
        username=signup_req.username,
        email=signup_req.email,
        password=signup_req.password_hash
    )
    return  user or None

class SignUpApiTestCase(APITestCase):
    def url(self):
        return 'http://localhost/api/auth/register/'

    def method(self):
        return 'POST'

    def test_create_user_when_success_then_insert_user_into_db(self):
        global email
        valid_data = {
            'username': 'nguyenduychien',
            'email': email,
            'password': 'Nguyenduychien1.',
        }

        res = self.send_request(data=valid_data)
        self.assertEqual(200, res.status_code)
        saved_signup = r.signup.find_one_by_email_or_username_in_signup_request(valid_data['email'], valid_data['username'])
        assert saved_signup
        self.assertEqual(saved_signup.username, valid_data['username'])
        self.assertEqual(saved_signup.email, valid_data['email'])

    def test_invalid_data(self):
        global data_test_register
        array_data = json.loads(data_test_register)
        results = []
        for valid_data in array_data:
            data = {
                'username': valid_data["username"],
                'email': valid_data["email"],
                'password': valid_data["password"],
            }
            res = self.send_request(data=data)
            results.append(valid_data["status_code"] == res.status_code)
        i = 1
        flag = True
        for result in results:
            if result == False:
                print("data_test_register error index: " + str(i))
                flag = False
            i += 1
        if flag:
            self.assertEqual(True, True)
        else:
            self.assertEqual(True, False)

class LoginApiTestCase(APITestCase):
    def url(self):
        return 'http://localhost/api/auth/login/'

    def method(self):
        return 'POST'

    def test_login(self):
        # create mock user data
        user = create_mock_user()
        user_test = r.user.find_user_by_username_and_email(user.username, user.email)
        # create req login
        valid_data = {
            'username': 'nguyenduychien',
            'password': 'Nguyenduychien1.',
        }
        self.send_request(data=valid_data)
        check_exist_user_token = m.User_Token.query.filter(
            m.User_Token.user_id == user_test.id
        ).first()
        self.assertEqual(check_exist_user_token.id, user_test.id)

class ResetPasswordApiTestCase(APITestCase):
    def url(self):
        return 'http://localhost/api/auth/resetPassword/'

    def method(self):
        return 'POST'

    def test_resetpassword_api(self):
        global email
        user = create_mock_user()
        valid_data = {
            'username' : 'nguyenduychien',
            'email' : email,
        }
        res = self.send_request(data=valid_data)
        self.assertEqual(200, res.status_code)

class ChangePasswordApiTestCase(APITestCase):
    def url(self):
        return 'http://localhost/api/auth/changePassword/'

    def method(self):
        return 'POST'

    def test_changepassword_api(self):
        user = create_mock_user()
        user_token = r.usertoken.create_token_by_user(user)
        valid_data = {
            'token' : user_token.token,
            'password' : 'Nguyenduychien1.',
            'newpassword' : 'Nguyenduychien2.',
        }
        res = self.send_request(data=valid_data)
        self.assertEqual(200, res.status_code)

class LogoutApiTestCase(APITestCase):
    def url(self):
        return 'http://localhost/api/auth/logout/'

    def method(self):
        return  'GET'

    def test_logout(self):
        user = create_mock_user()
        user_token = r.usertoken.create_token_by_user(user)
        headers = {
            'Authorization': user_token.token
        }
        print(user_token.token)

        self.send_request(headers=headers)
        find_user_token_test = r.usertoken.find_usertoken_by_tokenstring(user_token.token)
        self.assertEqual(find_user_token_test, None)

class VerifyApiTestCase(APITestCase):

    def method(self):
        return 'GET'

    def test_verify(self):
        global email
        mock_data = {
            'username': 'nguyenduychien',
            'email': email,
            'password': 'Nguyenduychien1.',
        }
        signup_req = r.signup.save_user_to_signup_request(
            **mock_data
        )
        url = 'http://localhost:5000/api/auth/register/verify/' + signup_req.user_token_confirm
        res = self.send_request(url=url)
        self.assertEqual(200, res.status_code)


