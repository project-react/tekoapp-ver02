from tekoapp import models
from datetime import datetime

def username_email_and_is_admin(new_username, new_email, new_is_admin, user):
    user.username = new_username
    user.email = new_email
    user.is_admin = new_is_admin
    user.updated_at = datetime.now()
    models.db.session.add(user)
    models.db.session.commit()
    return user

def look_time(user, look_time):
    user.look_time = look_time
    user.look_create_at = datetime.now()
    models.db.session.add(user)
    models.db.session.commit()
    return  user or None

def is_active(user, is_active):
    user.is_active = is_active
    models.db.session.add(user)
    models.db.session.commit()
    return user or None