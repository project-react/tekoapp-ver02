from tekoapp import helpers as h, repositories as r


def create_new(user):
    if user is None:
        return None
    else:
        new_password = h.random_password()
        r.user.edit.password(
            user=user,
            new_password=new_password
        )
        return new_password
