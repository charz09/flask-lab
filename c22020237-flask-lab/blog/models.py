from datetime import datetime
from blog import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(40), nullable=False, default='default.jpg')
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.date}', '{self.title}', '{self.content}')"

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # is_admin = db.Column(db.Boolean, nullable=False, default=False)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    post = db.relationship('Post', backref='user', lazy=True)

    def __repr__(self):
        return f"User('{self.username}')"

  #adated from Grinberg(2014, 2018)
    @property
    def password(self):
        raise AttributeError('Password is not readable.')

    @password.setter
    def password(self,password):
        self.hashed_password=generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash,password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

