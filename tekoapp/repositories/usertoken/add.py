from tekoapp import models

def by_user_model(user):
    data = {
        'user_id' : user.id,
    }
    token = models.User_Token(**data)
    models.db.session.add(token)
    models.db.session.commit()
    return token or None