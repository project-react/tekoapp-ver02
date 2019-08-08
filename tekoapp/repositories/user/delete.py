from tekoapp import models


def self(user):
    models.db.session.delete(user)
    models.db.session.commit()
