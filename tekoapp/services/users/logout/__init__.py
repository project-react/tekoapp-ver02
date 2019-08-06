from . import token

def make_response(tokenstring=""):
    return token.decode(
        tokenstring=tokenstring
    )