from tekoapp import repositories as r
from . import check, create


def make_response(token, email):
    if (
        check.token_data_with_email(
            access_token=token,
            email=email,
        )
        and
        check.email_not_exist_in_signup_model(
            email=email
        )
    ):
        user = r.user.find.by_email_or_username(
            email=email,
            username="",
        )
        if user:
            user_token = r.usertoken.add.by_user_model(
                user=user
            )
            return {
                'token': user_token.token,
                'username': user.username,
                'isAdmin': user.is_admin,
            }
        else:
            return create.new_user_by_email(
                email=email
            )

