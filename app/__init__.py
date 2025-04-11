from flask import Flask, jsonify
from dotenv import load_dotenv

from app.extensions import db, migrate, bcrypt, jwt
from app.extensions.jwt_handlers import register_jwt_callbacks
from app.extensions.error_handlers import register_error_handlers

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    # Initialize extensions
    initialize_extensions(app)

    # Register callbacks and handlers
    register_jwt_callbacks(jwt)
    register_error_handlers(app)

    # Register blueprints
    register_blueprints(app)

    # Only import models after extensions and blueprints are set up to avoid circular imports
    from app.models import User, Role, Permission

    # Default route
    @app.route('/')
    def home():
        return jsonify({"message": "Welcome to QuoteBook API"})

    return app


def initialize_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)


def register_blueprints(app):
    from app.routes.quote_routes import quote_bp
    from app.routes.auth_routes import auth_bp
    from app.routes.user_routes import user_bp

    app.register_blueprint(quote_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
