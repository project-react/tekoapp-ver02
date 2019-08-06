from tekoapp import models
from sqlalchemy import desc
from tekoapp.extensions import exceptions

def save_history_pass(userid, password, is_real_pass):
    data = {
        'user_id': userid,
        'password': password,
        'is_real_pass': is_real_pass
    }
    historypass = models.History_Pass_Change(**data)
    models.db.session.add(historypass)
    models.db.session.commit()
    return  historypass


def delete_history_password_by_id(id):
    hp = models.History_Pass_Change.query.filter(
        models.History_Pass_Change.id == id
    ).first()
    models.db.session.delete(hp)
    models.db.session.commit()


def delete_old_password(userid):
    listhistorypass = models.History_Pass_Change.query \
        .filter(models.History_Pass_Change.user_id == userid).all()
    sizelisthistorypass = len(listhistorypass)
    if (sizelisthistorypass > 5):
        listhistorypassdelete = models.History_Pass_Change.query\
        .filter(models.History_Pass_Change.user_id == userid)\
        .order_by(models.History_Pass_Change.created_at)\
        .limit(sizelisthistorypass - 5).all()
        for historypassdelete in listhistorypassdelete:
            delete_history_password_by_id(historypassdelete.id)
        return  True
    else:
        return False


def check_history_pass_when_change(userid, newpassword):
    listhistorypass = models.History_Pass_Change.query \
        .filter(models.History_Pass_Change.user_id == userid) \
        .order_by(desc(models.History_Pass_Change.created_at)) \
        .limit(5)\
        .all()

    for historypass in listhistorypass:
        if historypass.check_password(newpassword):
            return  False
    return True