import jwt, config
from tekoapp.extensions import exceptions
from tekoapp import repositories

def check_token_and_verify_admin(func):
    def inner(token):
        try:
            data = jwt.decode(token, config.FLASK_APP_SECRET_KEY)
            user = repositories.user.find_user_by_id(data['userid'])
            if user.is_admin:
                return func(token)
            else:
                raise exceptions.UnAuthorizedException(message='not authorized')
        except jwt.ExpiredSignature:
            repositories.usertoken.delete_token_by_tokenstring(token)
            raise exceptions.UnAuthorizedException('expired token, auto logout')
        except jwt.exceptions.InvalidTokenError:
            raise exceptions.BadRequestException('Invalid Token')
    return inner
