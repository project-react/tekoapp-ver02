import jwt
import config
from tekoapp import repositories as r

from tekoapp.extensions import exceptions


def decode(tokenstring=''):
    try:
        jwt.decode(tokenstring, config.FLASK_APP_SECRET_KEY)
        if r.usertoken.delete.by_tokenstring(
            tokenstring=tokenstring
        ):
            return {
                "message": "logout success",
            }
        else:
            raise exceptions.BadRequestException('token not exist')
    except jwt.ExpiredSignature:
        r.usertoken.delete.by_tokenstring(
            tokenstring=tokenstring
        )
        raise exceptions.UnAuthorizedException('expired token, auto logout')
    except jwt.exceptions.InvalidTokenError:
        raise exceptions.BadRequestException('Invalid Token')