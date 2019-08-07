from tekoapp import helpers as h

@h.verify.admin.by_token
def make_response(token):
    return True