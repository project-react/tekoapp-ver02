from tekoapp import repositories as r
from datetime import datetime, timedelta


def by_user_id(user_id):
    user = r.user.find.by_id(
        user_id=user_id,
    )
    if user:
        exp_time = datetime.timestamp(datetime.now() - timedelta(minutes=user.look_time))
        look_create_at = datetime.timestamp(user.look_create_at)
        if (exp_time - look_create_at) >= 0:
            r.user.edit.is_active(
                user=user,
                is_active=True,
            )
            return True
        else:
            return False
    else:
        return False


def by_user(user):
    if user:
        exp_time = datetime.timestamp(datetime.now() - timedelta(minutes=user.look_time))
        look_create_at = datetime.timestamp(user.look_create_at)
        if (exp_time - look_create_at) >= 0:
            r.user.edit.is_active(
                user=user,
                is_active=True
            )
            return True
        else:
            return False
    else:
        return False



