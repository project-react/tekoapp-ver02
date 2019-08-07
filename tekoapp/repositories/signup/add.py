from tekoapp import models


def by_data(**kwargs):
    user = models.SignupRequest(**kwargs)
    models.db.session.add(user)
    models.db.session.commit()
    return user
