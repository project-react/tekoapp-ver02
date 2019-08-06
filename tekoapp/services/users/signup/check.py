from tekoapp import repositories as r
from tekoapp.extensions import exceptions

def no_account(email, username):
    signup_request = r.signup.find.by_email_or_username(email, username)
    user = r.user.find.by_email_or_username(email, username)
    if (
        signup_request
        or
        user
    ):
        raise exceptions.BadRequestException(
            "User with username {username} "
            "or email {email} already existed!".format(
                username=username,
                email=email
            )
        )
    else:
        return True