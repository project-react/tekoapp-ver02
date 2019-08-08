from tekoapp import helpers as h, repositories as r
from tekoapp.extensions import exceptions as e
from . import check


@h.validator_before_handling
def make_response(username, password):
    user = check.exist_account(
        username=username,
        password=password,
    )
    if h.verify.lockaccount.by_user(
        user=user
    ):
        user_token = r.usertoken.add.by_user_model(
            user=user
        )
        return {
            'token': user_token.token,
            'isAdmin': user.is_admin,
        }
    else:
        raise e.UnAuthorizedException(message="Account locked")
