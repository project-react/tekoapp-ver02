import jwt
import config

from datetime import datetime
from tekoapp import repositories, helpers
from tekoapp.extensions import exceptions


@helpers.validator_before_handling
def check_info_from_login_request(username, password, **kwargs):
    user = repositories.user.find_user_by_username(username)
    if user is None:
        raise exceptions.UnAuthorizedException(message="Not found user")
    else:
        if(user.check_password(password)):
            # function add token
            if helpers.verify_look_account_by_user(user):
                user_token = repositories.usertoken.create_token_by_user(user)
                if user_token is None:
                    raise exceptions.UnAuthorizedException(message="Don't insert token")
                else:
                    timestr =  datetime.timestamp(user_token.expired_time)
                    return {
                        'token': user_token.token,
                        'expired_time': timestr,
                        'isAdmin': user.is_admin,
                    }
            else:
                raise exceptions.UnAuthorizedException(message="Account locked")
        else:
            raise exceptions.BadRequestException("Password invalid") 


def check_maintain_login(tokenstring=""):
    try:
        token_data = jwt.decode(tokenstring, config.FLASK_APP_SECRET_KEY)
        return {"message": "still valid"}
    except jwt.ExpiredSignature:
        repositories.usertoken.delete_token_by_tokenstring(tokenstring)
        raise exceptions.UnAuthorizedException('expired token, auto logout')
