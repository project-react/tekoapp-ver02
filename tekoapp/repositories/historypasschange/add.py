from tekoapp import models as m

def by_userid_and_password(
    userid,
    password,
    is_real_pass
):
    data = {
        'user_id': userid,
        'password': password,
        'is_real_pass': is_real_pass
    }
    historypass = m.History_Pass_Change(**data)
    m.db.session.add(historypass)
    m.db.session.commit()
    return historypass