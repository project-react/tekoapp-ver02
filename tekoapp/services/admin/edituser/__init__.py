from tekoapp import  repositories as r, helpers
from tekoapp.extensions import exceptions


@helpers.validator_before_handling
def edit_user(user_edited_id, new_username, new_email, is_admin, **kwargs):
   user = r.user.find.by_id(
       user_id=user_edited_id
   )
   # if user:
   #     if repositories.user.check_orther_user_had_username_email(user.id, new_username, new_email):
   #         if (
   #              user.username != new_username
   #              or
   #              user.email != new_email
   #              or
   #              user.is_admin != is_admin
   #         ):
   #             if repositories.user.edit_username_email_is_admin_in_user(new_username, new_email, is_admin, user):
   #                 return {
   #                     'message': 'edit success'
   #                 }
   #             else:
   #                 raise exceptions.BadRequestException('server error')
   #         else:
   #             raise exceptions.BadRequestException('User Unchanged')
   #     else:
   #         raise exceptions.BadRequestException('User name or email already exist')
   # else:
   #     raise exceptions.BadRequestException('Not found user')