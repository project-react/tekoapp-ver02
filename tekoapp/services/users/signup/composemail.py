import config
from tekoapp import helpers
from tekoapp.extensions import exceptions


def send(
    token_confirm='',
    email='',
):
    content_mail = '<a href="{0}/{1}/{2}">Click here</b>'.format(config.BASE_URL, 'api/users/register/verify',
                                                                 token_confirm)
    check_send = helpers.send_mail("Information Veriry Account.", content_mail, email, "verify")
    if check_send:
        return {
            "message": "success",
        }
    else:
        raise exceptions.HTTPException(message='mail server error')

