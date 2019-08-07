from tekoapp import repositories as r
from tekoapp.extensions import exceptions as e


def no_exist_in_user_model(
    username='',
    email='',
):
    if r.user.find.by_email_or_username(
        username=username,
        email=email,
    ):
        raise e.BadRequestException('Username or email already exist')
    else:
        return True


def no_exist_in_signup_request_model(
    username='',
    email='',
):
    if r.signup.find.by_email_or_username(
        username=username,
        email=email,
    ):
        raise e.BadRequestException('Username or email already exist')
    else:
        return True




