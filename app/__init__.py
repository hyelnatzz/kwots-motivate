from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_restful import Api

db = SQLAlchemy()



def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    api = Api(app)
    login_manager = LoginManager(app)
    login_manager.login_view = "auth_bp.login"

    from .auth import auth_bp
    from .quote import quote_bp
    from .user import user_bp
    from .views import main_bp
    from .api import api_bp
        
    app.register_blueprint(api_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(quote_bp)
    app.register_blueprint(main_bp)

    from .models import Color, Category, Quote, User
    

    @login_manager.user_loader
    def loader(user_id):
        return User.query.get(int(user_id))
    

    with app.app_context():
        db.create_all()
        return app

