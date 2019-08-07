import jwt
import config
from tekoapp.extensions import exceptions
from tekoapp import repositories as r


def by_token(func):
    def inner(token):
        try:
            data = jwt.decode(token, config.FLASK_APP_SECRET_KEY)
            user = r.user.find.by_id(
                user_id=data['user_id']
            )
            if user.is_admin:
                return func(token)
            else:
                raise exceptions.UnAuthorizedException(message='not authorized')
        except jwt.ExpiredSignature:
            r.usertoken.delete.by_tokenstring(
                tokenstring=token
            )
            raise exceptions.UnAuthorizedException('expired token, auto logout')
        except jwt.exceptions.InvalidTokenError:
            raise exceptions.BadRequestException('Invalid Token')
    return inner
