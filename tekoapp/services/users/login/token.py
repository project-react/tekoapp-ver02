import jwt
import config
from tekoapp import repositories as r
from tekoapp.extensions import exceptions as e

def decode(token_string):
    try:
        token_data = jwt.decode(token_string, config.FLASK_APP_SECRET_KEY)
        return {"message": "still valid"}
    except jwt.ExpiredSignature:
        r.usertoken.delete.by_tokenstring(
            tokenstring=token_string
        )
        raise e.UnAuthorizedException('expired token, auto logout')
    except jwt.exceptions.InvalidTokenError:
        raise e.BadRequestException('invalid token')