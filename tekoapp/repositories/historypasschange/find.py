from tekoapp import models as m
from sqlalchemy import desc

def five_recently(userid):
    return m.History_Pass_Change.query \
        .filter(m.History_Pass_Change.user_id == userid) \
        .order_by(desc(m.History_Pass_Change.created_at)) \
        .limit(5)\
        .all()

def by_userid(userid):
    return m.History_Pass_Change.query \
        .filter(m.History_Pass_Change.user_id == userid).all()

def first_n_element(userid, n):
    return m.History_Pass_Change.query \
        .filter(m.History_Pass_Change.user_id == userid) \
        .limit(n)
