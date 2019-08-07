from tekoapp import helpers as h, repositories as r
from . import tokengoogle
from tekoapp.extensions import  exceptions as e
from datetime import datetime

@h.validator_before_handling
def new_username_email_password(
    username="",
    email="",
    password=""
):
    return True


def token_data_with_email(
    access_token='',
    email='',
):
    token_data = tokengoogle.decode(
        access_token=access_token
    )
    if token_data['email'] == email:
        return True
    else:
        raise e.BadRequestException(
            message='Invalid email'
        )


def email_not_exist_in_signup_model(
    email='',
):
    signup_request = r.signup.find.by_email_or_username(
        email=email,
        username="",
    )
    if signup_request:
        raise e.BadRequestException(
            "Email {email} already register!, check email and verify a".format(
                email=email
            )
        )
    else:
        return True


