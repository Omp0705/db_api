from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

db = SQLAlchemy()  # Initialize SQLAlchemy
migrate = Migrate()  # Initialize Flask-Migrate
jwt = JWTManager()  # Initialize JWT

def create_app():
    app = Flask(__name__)
    
    # Configuration from config.py
    app.config.from_object('config.Config')

    # Initialize the extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Register blueprints (routes)
    from .routes import api_bp
    app.register_blueprint(api_bp)

    return app
