from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from views import views
from auth import auth
from models import db,User,StatData



app = Flask(__name__)
app.secret_key = 'aaaa'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Jani@localhost/fuel'
app.register_blueprint(views, url_prefix = '/')
app.register_blueprint(auth, url_prefix='/')
db.init_app(app=app)

#The db creation will be done through a python command from a terminal after importing both the db object from the models, and the app object from the main file to it

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
        return User.query.get(int(id))




if __name__ == '__main__':
        app.debug =True
        app.run()