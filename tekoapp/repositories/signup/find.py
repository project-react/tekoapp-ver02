from tekoapp import models
from sqlalchemy import or_

def by_email_or_username(email="", username=""):
    user_in_signup_request = models.Signup_Request.query.filter(
        or_(
            models.Signup_Request.username == username,
            models.Signup_Request.email == email
        )
    ).first()
    return user_in_signup_request or None

def by_token(token):
    return models.Signup_Request.query.filter(
        models.Signup_Request.user_token_confirm == token
    ).first() or None