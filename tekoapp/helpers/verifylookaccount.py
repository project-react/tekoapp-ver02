from tekoapp import repositories
from datetime import datetime, timedelta

def verify_look_account_by_username_email(username, email):
    user = repositories.user.find_user_by_username_and_email(
        username=username,
        email=email
    )
    if user:
        exp_time = datetime.timestamp(datetime.now() - timedelta(minutes=user.look_time))
        look_create_at = datetime.timestamp(user.look_create_at)
        if (exp_time - look_create_at >= 0):
            repositories.user.edit_is_active_in_user(user=user, is_active=True)
            return True
        else:
            return False
    else:
        return False

def verify_look_account_by_user(user):
    if user:
        exp_time = datetime.timestamp(datetime.now() - timedelta(minutes=user.look_time))
        look_create_at = datetime.timestamp(user.look_create_at)
        if (exp_time - look_create_at >= 0):
            repositories.user.edit_is_active_in_user(user=user, is_active=True)
            return True
        else:
            return False
    else:
        return False