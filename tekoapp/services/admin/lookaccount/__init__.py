from tekoapp import  repositories as r
from tekoapp.extensions import exceptions as e
from . import check


def make_response(token, user_id, look_time, **kwargs):
    locker_id = check.locker_id_is_admin(
        access_token=token
    )
    if (
        check.do_not_lock_myself(
            locker_id=locker_id,
            user_id=user_id,
        )
    ):
        user = r.user.find.by_id(
            user_id=user_id
        )
        if user:
            r.user.edit.look_time(
                user=user,
                look_time=look_time,
            )
            return {
                'msg': 'success'
            }
        else:
            raise e.BadRequestException('database error')