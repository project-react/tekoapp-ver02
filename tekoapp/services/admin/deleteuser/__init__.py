from tekoapp.extensions import exceptions as e
from tekoapp import repositories as r
from . import check


def make_response(token, user_id, **kwargs):
    eraser_id = check.eraser_id_is_admin(
        access_token=token
    )
    if (
        check.do_not_delete_your_self(
            eraser_id=eraser_id,
            user_id=user_id,
        )
    ):
        user=check.user_exist(
            user_id=user_id
        )
        if user.is_admin:
            raise e.UnAuthorizedException(
                message='un authorized'
            )
        else:
            r.user.delete.self(
                user=user
            )
            return {
                'msg': 'success'
            }
