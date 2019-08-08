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


def change_information(
    user,
    new_username='',
    new_email='',
    new_is_admin=False,
):
    if(
      user.username == new_username
      and
      user.email == new_email
      and
      user.is_admin == new_is_admin
    ):
        raise e.BadRequestException('Information Unchanged')
    else:
        return True


def exist_username_or_email_in_user(
    user_id,
    new_username='',
    new_email='',
):
    list_orther_user = r.user.find.list_orther_user(
        user_id=user_id
    )
    for user in list_orther_user:
        if(
            user.username == new_username
            or
            user.email == new_email
        ):
            raise e.BadRequestException('User name or email already exist')
    return True


def exist_username_or_email_in_signup_request(
    new_username='',
    new_email=''
):
    if r.signup.find.by_email_or_username(
        username=new_username,
        email=new_email,
    ):
        raise e.BadRequestException('User name or email already exist')
    else:
        return True
