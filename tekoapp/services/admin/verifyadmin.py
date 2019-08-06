from tekoapp import repositories, helpers
from tekoapp.extensions import exceptions

@helpers.check_token_and_verify_admin
def verify_is_admin_by_token(token):
    return True
