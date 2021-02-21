from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import query

db = SQLAlchemy()



def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)

    from .auth import auth_bp
    from .quote import quote_bp
    from .user import user_bp
    from .views import main_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(quote_bp)
    app.register_blueprint(main_bp)

    from .models import Color, Category, Quote, User
    
    def add_initial_data():
        color = Color()
        color.name = '#F723FB'
        color.save()
        category = Category()
        category.name = 'General'
        category.color = color
        category.save()

    with app.app_context():
        db.create_all()
        if not Category.query.all():
            add_initial_data()
        return app
