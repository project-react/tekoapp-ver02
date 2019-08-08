from tekoapp import repositories as r
from tekoapp.extensions import exceptions as e


def exist_account(user_id):
    user = r.user.find.by_id(
        user_id=user_id
    )
    if user:
        return user
    else:
        raise e.BadRequestException("account not exist!")


def password(password, user):
    if user.check_password(
            password=password
    ):
        return True
    else:
        raise e.UnAuthorizedException(message="Password invalid")


def history_password(user_id, new_password):
    list_five_history_password = r.historypasschange.find.five_recently(
        user_id=user_id
    )
    for history_pass in list_five_history_password:
        if history_pass.check_password(new_password):
            return False
    return True

