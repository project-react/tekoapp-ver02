from tekoapp import helpers as h
from . import  token, check, password as pw
from tekoapp.extensions import exceptions as e

@h.validator_before_handling
def make_response(
    access_token="",
    password="",
    new_password="",
    **kwargs
):
    token_data = token.decode(
        access_token=access_token
    )
    user_id = token_data["user_id"]
    user = check.exist_account(
        user_id=user_id
    )
    if check.password(
        password=password,
        user=user
    ):
        return pw.update(
            new_password=new_password,
            user=user,
        )
    else:
        raise e.UnAuthorizedException(message="Password invalid")

