from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    
    @app.route('/')
    def home():
        return jsonify({"message": "Welcome to QuoteBook API"})

    # Register Blueprints
    from app.routes.quote_routes import quote_bp
    from app.routes.auth_routes import auth_bp
    app.register_blueprint(quote_bp)
    app.register_blueprint(auth_bp)

    return app
