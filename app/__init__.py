from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
import os
import logging
from .main import main as main_blueprint
from .auth import auth as auth_blueprint
from .generative_ai import generative_ai as generative_ai_blueprint

def create_app():
    app = Flask(__name__)

    # Configure JWT with a secure secret key from environment variables
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

    # Initialize JWT
    jwt = JWTManager(app)

    # Register blueprints
    app.register_blueprint(main_blueprint, url_prefix='/main')
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(generative_ai_blueprint, url_prefix='/ai')

    # Configure logging
    logging.basicConfig(filename='logs/application.log', level=logging.INFO)

    # Root endpoint
    @app.route('/')
    def home():
        return jsonify({"message": "Welcome to the Insurance Claim Prediction API!"})

    # Error handling
    @app.errorhandler(404)
    def not_found_error(error):
        logging.warning(f"404 Not Found: {error}")
        return jsonify({"error": "Resource not found"}), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        logging.error(f"500 Internal Server Error: {error}")
        return jsonify({"error": "An internal server error occurred"}), 500

    return app

