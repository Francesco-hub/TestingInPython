from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app(environment):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    if(environment=='testing'):
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///projectTest.db"
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    db.init_app(app)

    from . import models

    with app.app_context():
        db.create_all()

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

