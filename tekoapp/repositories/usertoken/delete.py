from tekoapp import models
from tekoapp.repositories import usertoken


def by_token_string(token_string):
    user_token = usertoken.find.by_tokenstring(tokenstring=token_string)
    if user_token:
        models.db.session.delete(user_token)
        models.db.session.commit()
        return True
    else:
        return False

