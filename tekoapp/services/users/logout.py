import jwt
import config
from tekoapp import repositories

from tekoapp.extensions import exceptions

def check_token_from_logout_request(tokenstring):
    try:
        jwt.decode(tokenstring, config.FLASK_APP_SECRET_KEY)
        repositories.usertoken.delete_token_by_tokenstring(tokenstring)
        return {
                "message": "logout success",
            }
    except jwt.ExpiredSignature:
        repositories.usertoken.delete_token_by_tokenstring(tokenstring)
        raise exceptions.UnAuthorizedException('expired token, auto logout')
    except jwt.exceptions.InvalidTokenError:
        raise exceptions.BadRequestException('Invalid Token')

