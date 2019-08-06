import enum
import logging
from flask_restplus import fields
from datetime import datetime, timedelta


from tekoapp.models import db, bcrypt

class User(db.Model):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(191), nullable=False, unique=True)
    email = db.Column(db.String(191), nullable=False, unique=True)
    password_hash = db.Column(db.Text(), nullable=False)
    is_active = db.Column(db.Boolean, default=False)
    last_login = db.Column(db.TIMESTAMP, default = datetime.now())
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.TIMESTAMP, default = datetime.now())
    updated_at = db.Column(db.TIMESTAMP, default = datetime.now())
    look_time = db.Column(db.Integer, default = 0)
    look_create_at = db.Column(db.TIMESTAMP, default = datetime.now())

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(
            password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def get_id(self):
        return self.id

    def to_dict(self):
        """
        Transform user obj into dict
        :return:
        """
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
        }

class UserSchema:
    user_create_req = {
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
    }
    user_create_res = {
        'token': fields.String(required=True, description='token user'),
    }
    

