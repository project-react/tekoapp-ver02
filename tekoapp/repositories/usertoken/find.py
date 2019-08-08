from tekoapp import models

def by_tokenstring(tokenstring):
    return models.UserToken.query.filter(
        models.UserToken.token == tokenstring
    ).first()