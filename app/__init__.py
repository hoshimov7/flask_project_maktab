from flask import Flask
from app.extentions import db
from app.routes import main
from app.models import Post, Users
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)

    # Configure the database
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///school.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['SECRET_KEY'] = "alo-assalomualuaykn"
    db.init_app(app)


    # Create the database tables
    
    with app.app_context():
        db.create_all()


    #login 
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'  # Set the login view route

    @login_manager.user_loader
    def load_user(user_id):
        try:
            user_id = int(user_id)
        except ValueError:
            return None

        return db.session.get(Users, user_id)

    # Register blueprints
    app.register_blueprint(main)

    
    return app
