from tekoapp import repositories as r
from tekoapp import helpers as h
from tekoapp.extensions import exceptions as e


def new_user(
    username='',
    email='',
    is_admin=False,
):
    user = r.user.add.by_username_email_is_admin(
        username=username,
        email=email,
        is_admin=is_admin,
    )
    if user:
        password = user['password']
        content_mail = "Your Password: " + password
        send_mail = h.send_mail(
            subject='New Account',
            content_msg=content_mail,
            des_mail=email,
        )
        if send_mail:
            return {
                'msg': 'success'
            }
    else:
        raise e.NotFoundException(
            message="insert user to database error"
        )

