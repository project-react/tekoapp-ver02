from . import check, composemail, token
from tekoapp import helpers, repositories as r
from tekoapp.extensions import exceptions

@helpers.validator_before_handling
def make_response(username, email, password, **kwargs):
    if check.no_account(username=username, email=email):
        signup_request = r.signup.add.by_data(
            username=username,
            email=email,
            password=password,
            **kwargs
        )
        return composemail.send(
            token_confirm = signup_request.user_token_confirm,
            email=email,
        )

def verify(token_string):
    token_data = token.decode(tokenstring=token_string)
    username = token_data["username"]
    signup_request = r.signup.find.by_email_or_username(
        email="",
        username=username
    )
    if signup_request:
        r.signup.delete.self(signup_request)
        user = r.user.add.by_username_email_password(
            username=signup_request.username,
            email=signup_request.email,
            password=signup_request.password_hash
        )
        if user:
            return {
                'message': 'success',
            }
    else:
        raise exceptions.NotFoundException(message="not found user")
