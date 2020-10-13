from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from election.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from election.users.routes import users
    from election.posts.routes import posts
    from election.main.routes import main
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)

    return app



# # A bunch of really boring technical jargin
#
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# import os
# from flask_bcrypt import Bcrypt
# from flask_login import LoginManager
# from flask_mail import Mail  # We need a mail port and server
#
# # File Path
# UPLOAD_FOLDER = 'D:/uploads'
#
# # Connect with test database
# db_path = os.path.join(os.path.dirname(__file__), 'site.db')
# db_uri = 'sqlite:///{}'.format(db_path)
#
# # Start the web app
# app = Flask(__name__)
# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 530
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
# app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
# mail = Mail(app)
#
# # Configure the app's url and encryption key
# app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
# app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
#
# # Configure uploading files of any kind
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
#
#
# # Configure the web app's database
# db = SQLAlchemy(app)
#
# #Encrypt the web app
# bcrypt = Bcrypt(app)
#
# # Login Manager function for managing pages the user can access
# login_manager = LoginManager(app)
# login_manager.login_view = 'login'
# login_manager.login_message_category = 'info'
#
# # Don't move this import. It's specifically after everthing for a reason.
# from election.users.routes import users
# from election.posts.routes import posts
# from election.main.routes import main
#
# app.register_blueprint(main)
# app.register_blueprint(users)
# app.register_blueprint(posts)
#
