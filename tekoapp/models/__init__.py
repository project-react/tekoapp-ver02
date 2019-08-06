import flask_bcrypt as _fb
import flask_migrate as _fm
import flask_sqlalchemy as _fs

db = _fs.SQLAlchemy()
migrate = _fm.Migrate(db=db)
bcrypt = _fb.Bcrypt()

def init_app(app, **kwargs):
    db.app = app
    migrate.init_app(app)
    db.init_app(app)

from .signup import Signup_Request, SignupSchema
from .user import User, UserSchema
from .usertoken import User_Token, TokenSchema
from .historypasschange import History_Pass_Change