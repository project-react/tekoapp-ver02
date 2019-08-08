from tekoapp import models, repositories as r
from tekoapp.extensions import exceptions as e
from . import check


def update(new_password, user):
    if check.history_password(
        user_id=user.id,
        new_password=new_password
    ):
        r.historypasschange.add.by_user_id_and_password(
            user_id=user.id,
            password=new_password,
            is_real_pass=False
        )
        r.historypasschange.delete.more_than_five_data(
            user_id=user.id
        )
        r.user.edit.password(
            user=user,
            new_password=new_password,
        )
        return {
            'message': 'success'
        }
    else:
        raise e.UnAuthorizedException (
            message="You have retyped the same password 5 times"
        )