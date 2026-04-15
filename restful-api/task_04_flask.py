#!/usr/bin/python3
"""
A simple Flask API with user management
"""
from flask import Flask, jsonify, request


app = Flask(__name__)

# Istifadəçiləri yaddaşda saxlamaq üçün lüğət
users = {}


@app.route("/", strict_slashes=False)
def home():
    """Root endpoint"""
    return "Welcome to the Flask API!"


@app.route("/data", strict_slashes=False)
def get_usernames():
    """Returns a list of all usernames"""
    return jsonify(list(users.keys()))


@app.route("/status", strict_slashes=False)
def status():
    """Returns the API status"""
    return "OK"


@app.route("/users/<username>", strict_slashes=False)
def get_user(username):
    """Returns the full object for a specific username"""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"], strict_slashes=False)
def add_user():
    """Adds a new user to the API"""
    # JSON-un doğruluğunu yoxlayırıq
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    
    # Username mövcudluğunu yoxlayırıq
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    # Dublikat yoxlaması
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    
    # İstifadəçini əlavə edirik
    users[username] = data
    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
