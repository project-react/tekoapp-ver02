from tekoapp import repositories as r, helpers
from tekoapp.extensions import exceptions

@helpers.check_token_and_verify_admin
def make_response(token):
    users = r.user.find.all()
    if users:
        response = []
        for user in users:
            datetime = str(user.updated_at)
            e = {
                'user_id': user.id,
                'username': user.username,
                'email': user.email,
                'updated_at': datetime,
                'is_admin': user.is_admin,
                'is_active': user.is_active,
            }
            response.append(e)
        return response
    else:
        raise exceptions.UnAuthorizedException('Server error')