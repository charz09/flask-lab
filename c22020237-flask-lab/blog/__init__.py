# import os
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
# from flask_login import LoginManager


# app = Flask(__name__)
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///post.db'

# basedir = os.path.abspath(os.path.dirname(__file__))

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

# app.config['SECRET_KEY'] = '18b36fd59147aabd49785d408654cc4a2146c524480bd655'
# db = SQLAlchemy(app)



# bcrypt = Bcrypt(app)
# login_manager = LoginManager(app)
# login_manager.login_view = "login_page"
# login_manager.login_message_category = "info"
# from blog import routes




from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# from flask_admin import Admin
# from blog.views import AdminView
# from flask_admin.contrib.sqla import ModelView
# from blog.models import User, Post

# def create_app():
    
app = Flask(__name__)
app.config['SECRET_KEY'] = '<22abc7aef7bd5e104019ee7c3bf4005eae4a81adcb9395aa>'

# basedir = os.path.abspath(os.path.dirname(__file__))

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'blog.db')


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://c22020237:#Ayoade2020#@csmysql.cs.cf.ac.uk:3306/c22020237_flask_lab_db'

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

# @login_manager.user_loader
# def load_user(user_id):
#     return User.get(user_id)

from blog import routes

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
#from blog.views import AdminView
from blog.models import User, Post
admin = Admin(app,name='Admin panel', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))


