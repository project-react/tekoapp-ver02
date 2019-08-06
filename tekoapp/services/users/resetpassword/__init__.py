from tekoapp import helpers as h
from tekoapp.extensions import exceptions
from . import check, password

@h.validator_before_handling
def make_response(username, email, **kwargs):
    user = check.exist_account(
        username=username,
        email=email,
    )
    if h.verify.lookaccount.by_user(
        user=user
    ):
        newpassword = password.create_new(
            user=user
        )
        content_mail = "Your Password: " + newpassword
        check_password = h.send_mail("Reset Password", content_mail, email)
        if check_password:
            return {
                'message': 'Reset password success. You can check mail: ' + email,
            }
        else:
            raise exceptions.ForbiddenException(message="Send mail error")
    else:
        raise exceptions.UnAuthorizedException(message="Account locked")