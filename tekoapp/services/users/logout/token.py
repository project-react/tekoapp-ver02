import jwt
import config
from tekoapp import repositories as r

from tekoapp.extensions import exceptions


def decode(access_token=''):
    try:
        jwt.decode(access_token, config.FLASK_APP_SECRET_KEY)
        if r.usertoken.delete.by_token_string(
            token_string=access_token
        ):
            return {
                "message": "logout success",
            }
        else:
            raise exceptions.BadRequestException('token not exist')
    except jwt.ExpiredSignature:
        r.usertoken.delete.by_token_string(
            token_string=access_token
        )
        raise exceptions.UnAuthorizedException('expired token, auto logout')
    except jwt.exceptions.InvalidTokenError:
        raise exceptions.BadRequestException('Invalid Token')