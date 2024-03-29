from tekoapp import repositories as r
from tekoapp.extensions import exceptions
from . import token


def exist_account(username='', password=''):
    account = r.user.find.by_username(
        username=username
    )
    if account:
        if account.check_password(password):
            return account
        else:
            raise exceptions.BadRequestException(message="Password invalid")
    else:
        raise exceptions.UnAuthorizedException(message="Not found user")


def maintain(access_token):
    return token.decode(
        access_token=access_token
    )
