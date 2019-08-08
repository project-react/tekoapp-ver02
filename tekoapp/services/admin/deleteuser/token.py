from tekoapp import repositories as r
from tekoapp.extensions import exceptions as e
import jwt
import config


def decode(token):
    try:
        data = jwt.decode(token, config.FLASK_APP_SECRET_KEY)
        return data
    except jwt.ExpiredSignature:
        r.usertoken.delete.by_token_string(
            token_string=token
        )
        raise e.UnAuthorizedException('expired token, auto logout')
    except jwt.exceptions.InvalidTokenError:
        raise e.BadRequestException('Invalid Token')

