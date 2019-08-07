from tekoapp import models
from tekoapp.repositories import signup


def self(signup_request):
    models.db.session.delete(signup_request)
    models.db.session.commit()


def by_token(token):
    signup_request = signup.find.by_token(token=token)
    models.db.session.delete(signup_request)
    models.db.session.commit()
    return signup_request or None

