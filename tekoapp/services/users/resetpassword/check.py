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

