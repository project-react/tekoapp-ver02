from tekoapp import models

def by_tokenstring(tokenstring):
    return models.User_Token.query.filter(
        models.User_Token.token == tokenstring
    ).first()