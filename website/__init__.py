from flask import Flask

def create_app():
    app = Flask(__name__)
    #key (do not want in dev stuff)
    app.config['SECRET_KEY'] = 'ballinorwhatever'

    #registers blueprints
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app