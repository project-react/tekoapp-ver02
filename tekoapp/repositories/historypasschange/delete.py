from tekoapp import models as m
from . import find

def by_id(id):
    hp = m.History_Pass_Change.query.filter(
        m.History_Pass_Change.id == id
    ).first()
    m.db.session.delete(hp)
    m.db.session.commit()

def del_self(historypassword):
    m.db.session.delete(historypassword)
    m.db.session.commit()

def more_than_five_data(userid):
    listhistorypass = find.by_userid(
        userid=userid
    )
    sizelisthistorypass = len(listhistorypass)
    if (sizelisthistorypass > 5):
        listdelete  = find.first_n_element(
            userid=userid,
            n=sizelisthistorypass-5
        )
        for historypass in listdelete:
            del_self(
                historypassword=historypass
            )
        return True
    else:
        return False
