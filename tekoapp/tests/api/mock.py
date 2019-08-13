from tekoapp import repositories as r


def account_is_user():
    return r.user.add.by_username_email_is_admin(
        username='chiennguyen99',
        email='duychien226@gmail.com',
        is_admin=False,
    )


def account_is_admin():
    return r.user.add.by_username_email_is_admin(
        username='nguyenduychien',
        email='besora@getvmail.net',
        is_admin=True,
    )

