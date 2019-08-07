from tekoapp import models as m
from sqlalchemy import desc


def five_recently(user_id):
    return m.HistoryPassChange.query \
        .filter(m.HistoryPassChange.user_id == user_id) \
        .order_by(desc(m.HistoryPassChange.created_at)) \
        .limit(5)\
        .all()


def by_user_id(user_id):
    return m.HistoryPassChange.query \
        .filter(m.HistoryPassChange.user_id == user_id).all()


def first_n_element(user_id, n):
    return m.HistoryPassChange.query \
        .filter(m.HistoryPassChange.user_id == user_id) \
        .limit(n)
