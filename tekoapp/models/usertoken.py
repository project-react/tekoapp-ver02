from flask_restplus import fields
from datetime import datetime, timedelta
import jwt, config
from tekoapp.models import db, bcrypt

class User_Token(db.Model):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.expired_time = (datetime.now() + timedelta(minutes=30))
        self.create_token()
    
    __tablename__ = 'user_token'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    token = db.Column(db.Text(), nullable=False)
    expired_time = db.Column(db.TIMESTAMP, nullable=False)
    created_at = db.Column(db.TIMESTAMP, default=datetime.now())

    def create_token(self):
        print(self.expired_time)
        token_data = {
            "userid" : self.user_id,
            "exp" : datetime.timestamp(self.expired_time)
        }
        token_string = jwt.encode(token_data, config.FLASK_APP_SECRET_KEY)
        token_string = str(token_string)[2:-1]
        self.token = token_string

class TokenSchema:
    token_create_res = {
        'expired_time': fields.String(required=True, description='expired time'),
        'token': fields.String(required=True, description='string token'),
    }