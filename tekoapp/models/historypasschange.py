import enum
import logging
from flask_restplus import fields
from datetime import datetime, timedelta


from tekoapp.models import db, bcrypt


class History_Pass_Change(db.Model):
    def __init__(self, **kwargs):
        pass_word = ''
        for k, v in kwargs.items():
            if (k == 'password'):
                pass_word = v
            elif (k == 'is_real_pass'):
                print(pass_word)
                self.set_password(pass_word, v)
            elif (k != 'password'):
                setattr(self, k, v)

    __tablename__ = 'history_pass_changes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    created_at = db.Column(db.TIMESTAMP, default=datetime.now())
    pass_change_history = db.Column(db.Text(), nullable=False)

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    def set_password(self, password, is_real_pass):
        if is_real_pass:
            if is_real_pass == False:
                self.pass_change_history = bcrypt.generate_password_hash(
                    password).decode('utf-8')
            elif is_real_pass == True:
                self.pass_change_history = password
        else:
            self.pass_change_history = bcrypt.generate_password_hash(
                password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.pass_change_history, password)

