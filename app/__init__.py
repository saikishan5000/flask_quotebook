from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    
    @app.route('/')
    def home():
        return jsonify({"message": "Welcome to QuoteBook API"})

    # Register Blueprints
    from app.routes.quote_routes import quote_bp
    app.register_blueprint(quote_bp)

    return app
