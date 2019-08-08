from tekoapp import helpers as h
from . import check, create


@h.validator_before_handling
def make_response(username='', email='', is_admin='', **kwargs):
    if (
        check.no_exist_in_user_model(
            username=username,
            email=email,
        )
        and
        check.no_exist_in_signup_request_model(
            username=username,
            email=email,
        )
    ):
        return create.new_user(
            username=username,
            email=email,
            is_admin=is_admin,
        )

