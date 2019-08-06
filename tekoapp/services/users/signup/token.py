import jwt
from tekoapp import repositories as r
from tekoapp.extensions import exceptions
def decode(tokenstring):
    try:
        token_data = jwt.decode(token_string, config.FLASK_APP_SECRET_KEY)
        return token_data
    except jwt.ExpiredSignature:
        delete_signup_request = r.signup.delete.by_token(tokenstring)
        if delete_signup_request:
            raise exceptions.UnAuthorizedException('expired token, delete account')
        else:
            raise exceptions.BadRequestException('database error')
    except jwt.exceptions.InvalidTokenError:
        raise exceptions.BadRequestException('Invalid Token')