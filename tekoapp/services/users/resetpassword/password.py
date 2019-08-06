from tekoapp import helpers as h, repositories as r
from . import check

def create_new(user):
    if user is None:
        return None
    else:
        newpassword = ''
        is_loop = True
        while(is_loop):
            newpassword = h.random_password()
            is_loop = False == check.historypassword(
                userid=user.id,
                newpassword=newpassword
            )

        r.historypasschange.add.by_userid_and_password(
            userid=user.id,
            password=newpassword,
            is_real_pass=False
        )
        r.historypasschange.delete.more_than_five_data(
            userid=user.id
        )
        r.user.edit.password(
            user=user,
            newpassword=newpassword
        )
        return newpassword
