from tekoapp import models as m
from . import find


def by_id(id):
    hp = m.HistoryPassChange.query.filter(
        m.HistoryPassChange.id == id
    ).first()
    m.db.session.delete(hp)
    m.db.session.commit()


def del_self(history_password):
    m.db.session.delete(history_password)
    m.db.session.commit()


def more_than_five_data(user_id):
    list_history_pass = find.by_user_id(
        user_id=user_id
    )
    size_list_history_pass = len(list_history_pass)
    if size_list_history_pass > 5:
        list_delete = find.first_n_element(
            user_id=user_id,
            n=size_list_history_pass - 5
        )
        for history_pass in list_delete:
            del_self(
                history_password=history_pass
            )
        return True
    else:
        return False
