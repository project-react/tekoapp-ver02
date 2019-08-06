from tekoapp import helpers as h
from . import  token, check, password as pw
from tekoapp.extensions import exceptions as e

@h.validator_before_handling
def make_response(
    tokenstring="",
    password="",
    newpassword="",
    **kwargs
):
    token_data = token.decode(
        tokenstring=tokenstring
    )
    user_id = token_data["userid"]
    user = check.exist_account(
        user_id=user_id
    )
    if check.password(
        password=password,
        user=user
    ):
        return pw.update(
            newpassword=newpassword,
            user=user,
        )
    else:
        raise e.UnAuthorizedException(message="Password invalid")