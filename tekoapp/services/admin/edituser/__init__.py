from tekoapp import repositories as r, helpers as h
from . import check


@h.validator_before_handling
def make_response(user_edited_id, new_username, new_email, new_is_admin, **kwargs):
    user_edited = check.exist_account(
        user_id=user_edited_id
    )
    if(
        check.exist_username_or_email_in_user(
            user_id=user_edited_id,
            new_username=new_username,
            new_email=new_email,

        )
        and
        check.exist_username_or_email_in_signup_request(
            new_username=new_username,
            new_email=new_email,
        )
        and
        check.change_information(
            user=user_edited,
            new_username=new_username,
            new_email=new_email,
            new_is_admin=new_is_admin
        )
    ):
        if r.user.edit.username_email_and_is_admin(
            new_username=new_username,
            new_email=new_email,
            new_is_admin=new_is_admin,
            user=user_edited
        ):
            return {
                'msg': 'success'
            }

