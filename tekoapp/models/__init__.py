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


from .signup import SignupRequest, SignupSchema
from .user import User, UserSchema
from .usertoken import UserToken, TokenSchema
from .historypasschange import HistoryPassChange


