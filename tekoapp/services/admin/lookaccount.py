import jwt, config
from tekoapp import  repositories, helpers
from tekoapp.extensions import exceptions

@helpers.validator_before_handling
def look_account_by_admin(token, username, email, look_time, **kwargs):
    try:
        data = jwt.decode(token, config.FLASK_APP_SECRET_KEY)
        user_admin = repositories.user.find_user_by_id(data['userid'])
        if user_admin.is_admin:
            if (
                user_admin.username != username
                or
                user_admin.email != email
            ):
                user = repositories.user.find_user_by_username_and_email(username=username, email=email)
                if user:
                    if repositories.user.edit_look_time_in_user(user, look_time):
                        return {
                            'message': 'success'
                        }
                    else :
                        raise exceptions.BadRequestException(message='database error')
                else:
                    raise  exceptions.BadRequestException(message='')
            else:
                raise exceptions.BadRequestException("This is your account, delete error")
        else:
            raise exceptions.UnAuthorizedException(message='not authorized')
    except jwt.ExpiredSignature:
        repositories.usertoken.delete_token_by_tokenstring(token)
        raise exceptions.UnAuthorizedException('expired token, auto logout')
    except jwt.exceptions.InvalidTokenError:
        raise exceptions.BadRequestException('Invalid Token')