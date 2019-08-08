from . import token
from tekoapp import repositories as r
from tekoapp.extensions import exceptions as e


def eraser_id_is_admin(access_token):
    token_data = token.decode(
        token=access_token
    )
    user_id = token_data['user_id']
    user = r.user.find.by_id(
        user_id=user_id
    )
    if user.is_admin:
        return user_id
    else:
        raise e.UnAuthorizedException(message='not authorized')


def do_not_delete_your_self(
    eraser_id,
    user_id
):
    if eraser_id == user_id:
        raise e.BadRequestException(
            message='This is your account, delete error'
        )
    else:
        return True


def user_exist(
    user_id
):
    user = r.user.find.by_id(
        user_id=user_id
    )
    if user:
        return user
    else:
        raise e.BadRequestException(
            message='not found user'
        )
