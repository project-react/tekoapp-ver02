from tekoapp import models


def by_access_token(access_token):
    return models.UserToken.query.filter(
        models.UserToken.token == access_token
    ).first()


def by_user_id(user_id):
    return models.UserToken.query.filter(
        models.UserToken.user_id == user_id
    ).first()

