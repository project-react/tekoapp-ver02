from tekoapp import models

def delete_one_by_email_or_username_in_user(user):
    models.db.session.delete(user)
    models.db.session.commit()