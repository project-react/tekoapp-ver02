from tekoapp import repositories, helpers

from tekoapp.extensions import exceptions

@helpers.validator_before_handling
def check_info_form_resetpassword_and_res(username, email, **kwargs):
    user = repositories.user.find_user_by_username_and_email(username, email)
    if user is None:
        raise exceptions.BadRequestException("user not exist!")
    else:
        #update value user in database
        if helpers.verify_look_account_by_user(user):
            newpassword = repositories.resetpassword.change_password(user)
            content_mail = "Your Password: " + newpassword
            check_password = helpers.send_mail("Reset Password", content_mail, email)
            if check_password:
                return {
                    'message': 'Reset password success. You can check mail: ' + email,
                }
            else:
                raise exceptions.ForbiddenException(message="Send mail error")
        else:
            raise exceptions.UnAuthorizedException(message="Account locked")