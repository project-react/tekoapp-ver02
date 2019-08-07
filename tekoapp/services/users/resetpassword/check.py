from tekoapp import repositories as r
from tekoapp.extensions import exceptions as e

def exist_account(username='', email=''):
    user = r.user.find.by_username_and_email(
        username=username,
        email=email,
    )
    if user:
        return user
    else:
        raise e.BadRequestException("account not exist!")

def historypassword(userid, newpassword):
    list_five_historypassword = r.historypasschange.find.five_recently(
        user_id=userid
    )
    for historypass in list_five_historypassword:
        if historypass.check_password(newpassword):
            return  False
    return True