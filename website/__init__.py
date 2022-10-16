from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from os import path
#tells flask we have logins
from flask_login import LoginManager

#inits internal database >:)
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    #key (do not want in dev stuff)
    app.config['SECRET_KEY'] = 'ballinorwhatever'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)


    #registers blueprints
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from . import models

    #does not overwrite a preexisting db.
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    #where should flask redirect us if the users not logged in and the login is required.
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    from .models import User
    @login_manager.user_loader
    def load_user(id):
        #tells flask how we load a user
        #user.query.get uses the primary key.
        return User.query.get(int(id))

    return app



