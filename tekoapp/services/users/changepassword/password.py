from tekoapp import models, repositories as r
from tekoapp.extensions import exceptions as e
from . import check


def update(newpassword, user):
    if check.historypassword(
        userid=user.id,
        newpassword=newpassword
    ):
        r.historypasschange.add.by_userid_and_password(
            userid=user.id,
            password=newpassword,
            is_real_pass= False
        )
        r.historypasschange.delete.more_than_five_data(
            userid=user.id
        )
        r.user.edit.password(
            user=user,
            newpassword=newpassword,
        )
        return {
            'message': 'success'
        }
    else:
        raise e.UnAuthorizedException (
            message="You have retyped the same password 5 times"
        )