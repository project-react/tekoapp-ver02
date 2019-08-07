from tekoapp import repositories as r
from tekoapp.extensions import exceptions as e
from . import token

def locker_id_is_admin(access_token):
    token_data = token.decode(
        access_token=access_token
    )
    locker_id=token_data['userid']
    locker = r.user.find.by_id(
        user_id=locker_id
    )
    if locker.is_admin:
        return locker_id
    else:
        raise e.UnAuthorizedException(message='not authorized')

def do_not_lock_myself(
    locker_id,
    user_id,
):
    if locker_id == user_id:
        raise e.UnAuthorizedException(message='This is your account, lock error')
    else:
        return True