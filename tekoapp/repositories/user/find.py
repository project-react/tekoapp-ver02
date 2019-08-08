from tekoapp import models, helpers as h
from sqlalchemy import or_, and_


def by_username(username=""):
    user = models.User.query.filter(
        models.User.username == username
    ).first()
    return user or None


def by_id(user_id):
    user = models.User.query.filter(
        models.User.id == user_id
    ).first()
    return user or None


def by_username_and_email(username="", email=""):
    user = models.User.query.filter(
        and_(
            models.User.username == username,
            models.User.email == email
        )
    ).first()
    return user or None


def by_email_or_username(email="", username=""):
    user = models.User.query.filter(
        or_(
            models.User.username == username,
            models.User.email == email
        )
    ).first()
    return user or None


def list_orther_user(
    user_id
):
    return models.User.query\
        .filter(models.User.id != user_id).all()


def all():
    db_user = models.User.query;
    for u in db_user:
        h.verify.lockaccount.by_user(u)
    return db_user.all()
