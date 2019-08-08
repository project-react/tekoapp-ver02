from . import token


def make_response(access_token=""):
    return token.decode(
        access_token=access_token
    )

