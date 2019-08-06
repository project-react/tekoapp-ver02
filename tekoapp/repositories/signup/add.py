from tekoapp import  models

def by_data(**kwargs):
    user = models.Signup_Request(**kwargs)
    models.db.session.add(user)
    models.db.session.commit()
    return user
