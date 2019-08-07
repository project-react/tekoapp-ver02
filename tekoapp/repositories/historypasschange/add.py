from tekoapp import models as m


def by_user_id_and_password(
    user_id,
    password,
    is_real_pass
):
    data = {
        'user_id': user_id,
        'password': password,
        'is_real_pass': is_real_pass
    }
    history_pass = m.HistoryPassChange(**data)
    m.db.session.add(history_pass)
    m.db.session.commit()
    return history_pass

