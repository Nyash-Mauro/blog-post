import os
from flask import Flask
from config import config_options
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet,configure_uploads
from flask_mail import Mail


app = Flask(__name__)
bootstrap = Bootstrap()
db = SQLAlchemy()
photos = UploadSet('photos')
mail = Mail()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(Configname):
    app.config.from_object(config_options[Configname])
    login_manager.init_app(app)
    db.init_app(app)
    mail.init_app(app)

    # configure_uploads(app,photos)    

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app