from tekoapp import helpers as h, repositories as r
from tekoapp.extensions import exceptions as e
from . import check
from datetime import datetime


@h.validator_before_handling
def make_response(username, password):
    user = check.exist_account(
        username=username,
        password=password,
    )
    if h.verify.lookaccount.by_user(
        user=user
    ):
        user_token = r.usertoken.add.by_user_model(
            user=user
        )
        exp_time = datetime.timestamp(user_token.expired_time)
        return {
            'token': user_token.token,
            'expired_time': exp_time,
            'isAdmin': user.is_admin,
        }
    else:
        raise e.UnAuthorizedException(message="Account locked")
