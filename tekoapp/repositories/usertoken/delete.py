from tekoapp import models
from tekoapp.repositories import usertoken

def by_tokenstring(tokenstring):
    user_token = usertoken.find.by_tokenstring(tokenstring=tokenstring)
    if user_token:
        models.db.session.delete(user_token)
        models.db.session.commit()
        return True
    else:
        return False