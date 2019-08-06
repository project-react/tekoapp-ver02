from tekoapp import  repositories, helpers
from tekoapp.extensions import exceptions

@helpers.validator_before_handling
def create_user_by_account_admin(username, email, is_admin, **kwargs):
    user_check_exist_in_user = repositories.user.find_one_by_email_or_username_in_user(
        email=email,
        username=username
    )
    user_check_exist_in_signup = repositories.signup.find_one_by_email_or_username_in_signup_request(
        email=email,
        username=username
    )
    if (
        user_check_exist_in_user
        or
        user_check_exist_in_signup
    ):
        raise exceptions.BadRequestException(message='Username or email already exist')
    else:
        new_user = repositories.user.add_user_by_username_and_email(
            username=username,
            email=email,
            is_admin=is_admin,
        )
        if new_user:
            print(new_user)
            password = new_user['password']
            content_mail = "Your Password: " + password
            send_mail = helpers.send_mail("New Account", content_mail, email)
            if send_mail:
                return {
                    'message': 'success'
                }
            else:
                raise exceptions.HTTPException(message='Send mail error')
        else:
            raise exceptions.BadRequestException(message='Database error')
