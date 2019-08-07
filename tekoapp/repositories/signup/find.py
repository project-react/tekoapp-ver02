from tekoapp import models
from sqlalchemy import or_


def by_email_or_username(email="", username=""):
    user_in_signup_request = models.SignupRequest.query.filter(
        or_(
            models.SignupRequest.username == username,
            models.SignupRequest.email == email
        )
    ).first()
    return user_in_signup_request or None


def by_token(token):
    return models.SignupRequest.query.filter(
        models.SignupRequest.user_token_confirm == token
    ).first() or None
