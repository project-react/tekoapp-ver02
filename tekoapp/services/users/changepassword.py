import jwt
import config

from tekoapp.extensions import exceptions
from tekoapp import repositories, helpers

@helpers.validator_before_handling
def check_info_and_res(token="", password="" ,newpassword="", **kwarg):
    try:
        token_data = jwt.decode(token, config.FLASK_APP_SECRET_KEY)
    except jwt.ExpiredSignature:
        repositories.usertoken.delete_token_by_tokenstring(token)
        raise exceptions.UnAuthorizedException('expired token, auto logout')
    except jwt.exceptions.InvalidTokenError:
        raise exceptions.BadRequestException('Invalid Token')

    user_id = token_data["userid"]
    user = repositories.user.find_user_by_id(user_id)
    if user is None:
        raise exceptions.BadRequestException("User not exist!")
    else:
        if (user.check_password(password)):
            if repositories.changepassword.update_password(newpassword, user):
                return {
                    "message": "Change password success",
                }
            else:
                raise exceptions.UnAuthorizedException(message="new password equal password")
        else:
            raise exceptions.UnAuthorizedException(message="Password invalid")