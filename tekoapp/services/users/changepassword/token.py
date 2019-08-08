import jwt
import config
from tekoapp import repositories as r
from tekoapp.extensions import exceptions


def decode(access_token):
    try:
        token_data = jwt.decode(access_token, config.FLASK_APP_SECRET_KEY)
        return token_data
    except jwt.ExpiredSignature:
        delete_signup_request = r.signup.delete.by_token(access_token)
        if delete_signup_request:
            raise exceptions.UnAuthorizedException('expired token, delete account')
        else:
            raise exceptions.BadRequestException('database error')
    except jwt.exceptions.InvalidTokenError:
        raise exceptions.BadRequestException('Invalid Token')