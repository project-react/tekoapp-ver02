from tekoapp import repositories as r
from tekoapp.extensions import exceptions as e
import jwt
import config


def decode(access_token):
    try:
        return jwt.decode(access_token, config.FLASK_APP_SECRET_KEY)
    except jwt.ExpiredSignature:
        r.usertoken.delete.by_token_string(access_token)
        raise e.UnAuthorizedException('expired token, auto logout')
    except jwt.exceptions.InvalidTokenError:
        raise e.BadRequestException('invalid token')