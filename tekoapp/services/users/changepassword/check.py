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

def historypassword(userid, newpassword):
    list_five_historypassword = r.historypasschange.find.five_recently(
        userid=userid
    )
    for historypass in list_five_historypassword:
        if historypass.check_password(newpassword):
            return  False
    return True