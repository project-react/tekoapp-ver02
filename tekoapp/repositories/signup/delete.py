from tekoapp import  models
from tekoapp.repositories import signup

def self(Signup_Request):
    models.db.session.delete(Signup_Request)
    models.db.session.commit()

def by_token(token):
    Signup_Request = signup.find.by_token(token=token)
    models.db.session.delete(Signup_Request)
    models.db.session.commit()
    return Signup_Request or None