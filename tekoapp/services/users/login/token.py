import jwt
import config
from tekoapp import repositories as r
from tekoapp.extensions import exceptions as e


def decode(access_token):
    try:
        token_data = jwt.decode(access_token, config.FLASK_APP_SECRET_KEY)
        return {"message": "still valid"}
    except jwt.ExpiredSignature:
        r.usertoken.delete.by_token_string(
            token_string=access_token
        )
        raise e.UnAuthorizedException('expired token, auto logout')
    except jwt.exceptions.InvalidTokenError:
        raise e.BadRequestException('invalid token')