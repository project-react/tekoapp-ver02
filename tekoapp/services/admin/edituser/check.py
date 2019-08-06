from tekoapp import repositories as r
from tekoapp.extensions import exceptions as e

def exist_account(user_id):
    user = r.user.find.by_id(
        user_id=user_id
    )
    if user:
        return user
    else:
        raise e.BadRequestException('Account not existed')


