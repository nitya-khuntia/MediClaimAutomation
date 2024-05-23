from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

# Define the authentication blueprint
auth = Blueprint('auth', __name__)

# Login endpoint to generate JWT
@auth.route('/login', methods=['POST'])
def login():
    # Simulate a user database
    user_database = {"admin": "password123"}  # Example user and password

    # Get login data
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # Validate credentials
    if username in user_database and user_database[username] == password:
        # Create JWT token
        access_token = create_access_token(identity=username)
        return jsonify({"access_token": access_token})

    # Unauthorized access
    return jsonify({"error": "Invalid credentials."}), 401
