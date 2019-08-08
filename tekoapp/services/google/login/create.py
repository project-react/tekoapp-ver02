from tekoapp import helpers as h, repositories as r
from tekoapp.extensions import exceptions as e
from . import check
from datetime import datetime


def create_official_username(
    username=''
):
    new_username = ''
    for c in username:
        if(
            (c >= '0') and (c <= '9')
            or
            (c >= 'a') and (c <= 'z')
        ):
            new_username = new_username + c
        else:
            new_username = new_username + str(ord(c))
    if len(new_username) < 6:
        new_username = new_username + 'tekoapp'
    return new_username


def new_user_by_email(
    email=''
):
    current_username = email.split('@')[0]
    username = create_official_username(
        username=current_username,
    )
    password = h.random_password()
    if check.new_username_email_password(
        username=username,
        email=email,
        password=password,
    ):
        data_user = {
            'username': username,
            'email': email,
            'password': password,
            'is_admin': False,
            'is_activate': True
        }
        user = r.user.add.by_data(data_user)
        if user:
            user_token = r.usertoken.add.by_user_model(
                user=user
            )
            return {
                'token': user_token.token,
                'username': user.username,
                'isAdmin': user.is_admin,
            }
        else:
            raise e.NotFoundException(
                message='database error'
            )



