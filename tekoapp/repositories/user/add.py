from tekoapp import helpers, models


def by_username_email_is_admin(username, email, is_admin):
    password = helpers.random_password()
    user = {
        'username': username,
        'email': email,
        'password': password,
        'is_admin': is_admin,
        'is_active': True
    }
    new_user = models.User(**user)
    models.db.session.add(new_user)
    models.db.session.commit()
    if new_user:
        return {
            'info': new_user,
            'password': password
        }
    return None


def by_data(data):
    user = models.User(**data)
    models.db.session.add(user)
    models.db.session.commit()
    return user or None


def by_username_email_password(username="", email="", password=""):
    data = {
        'username': username,
        'email': email,
        'password_hash': password,
        'is_active': 1
    }
    user = models.User(**data)
    models.db.session.add(user)
    models.db.session.commit()
    return user or None

