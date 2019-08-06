import jwt
from datetime import datetime
from tekoapp import helpers, repositories
from tekoapp.extensions import exceptions
from authlib.client import OAuth2Session
import google.oauth2.credentials
import googleapiclient.discovery

def build_credentials(access_token):
    access_token = access_token
    return google.oauth2.credentials.Credentials(
        access_token,
    )

def get_user_info(access_token):
    credentials = build_credentials(access_token)
    oauth2_client = googleapiclient.discovery.build(
        'oauth2', 'v2',
        credentials=credentials)
    return oauth2_client.userinfo().get().execute() or None

def create_username(username):
    newusername = ''
    for c in username:
        if (
            c >= '0' and c <= '9'
            or
            c >= 'a' and c <= 'z'
        ):
            newusername = newusername + c
        else:
            newusername = newusername + str(ord(c))
    if (len(newusername) < 6):
        newusername = newusername + 'tekoapp'
    return newusername

@helpers.validator_before_handling
def validate_username_email(username="", email="", password=""):
    return True

def create_password():
    return helpers.random_password()

def make_response(token, email):
    data_user_info = get_user_info(access_token=token)
    if data_user_info['email'] == email:
        existed_user = repositories.user.find_one_by_email_or_username_in_user(
            email=email, username="")
        existed_user_not_verify = repositories.signup.find_one_by_email_or_username_in_signup_request(
            email=email, username="")
        if (
            existed_user
        ):
            user_token = repositories.usertoken.create_token_by_user(existed_user)
            timestr = datetime.timestamp(user_token.expired_time)
            return {
                'token': user_token.token,
                'expired_time': timestr,
                'username': existed_user.username,
                'isAdmin': existed_user.is_admin,
            }
        elif existed_user_not_verify:
            raise exceptions.BadRequestException(
                "Email {email} already existed!".format(
                    email=email
                )
            )
        else:
            current_username = email.split('@')[0]
            username = create_username(current_username)
            password = create_password()
            if validate_username_email(username=username, email=email, password=password):
                data = {
                    'username': username,
                    'email': email,
                    'password': password,
                    'is_admin': False,
                    'is_active': True
                }
                user = repositories.user.add(data)
                if user:
                    user_token = repositories.usertoken.create_token_by_user(user)
                    timestr = datetime.timestamp(user_token.expired_time)
                    return {
                        'token': user_token.token,
                        'expired_time': timestr,
                        'isAdmin': user.is_admin,
                    }
    else:
        raise exceptions.BadRequestException('Invalid email')