#!/usr/bin/python3
"""
API Security: Basic Auth, JWT and Role-based Access Control
"""
from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
)

app = Flask(__name__)

# JWT üçün gizli açar
app.config['JWT_SECRET_KEY'] = 'super-secret-key-change-me'
jwt = JWTManager(app)
auth = HTTPBasicAuth()

# Istifadəçi bazası (Yaddaşda)
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# --- Basic Authentication Hissəsi ---

@auth.verify_password
def verify_password(username, password):
    """Basic Auth üçün parol yoxlaması"""
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username
    return None

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """Basic Auth ilə qorunan endpoint"""
    return "Basic Auth: Access Granted"

# --- JWT Authentication Hissəsi ---

@app.route('/login', methods=['POST'])
def login():
    """Giriş edib JWT token almaq üçün endpoint"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400
        
    username = data.get('username')
    password = data.get('password')
    
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        # Tokenin içinə istifadəçi rolunu da əlavə edirik
        access_token = create_access_token(
            identity=username, 
            additional_claims={"role": user['role']}
        )
        return jsonify(access_token=access_token)
    
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """JWT ilə qorunan endpoint"""
    return "JWT Auth: Access Granted"

# --- Role-based Access Control (RBAC) ---

@app.route('/admin-only')
@jwt_required()
def admin_only():
    """Yalnız adminlərin girə biləcəyi endpoint"""
    claims = get_jwt()
    if claims.get('role') != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

# --- Xüsusi JWT Error Handlerlər (401 qaytarması üçün) ---

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
