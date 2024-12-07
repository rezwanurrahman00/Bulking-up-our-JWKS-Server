"""
Author: Rezwanur Rahman
Course: CSCE 3550 - Foundations of Cybersecurity
Date: December 6, 2024
Description: Flask application for enhancing security and user management
in the JWKS Server using AES encryption, user registration, and authentication logging.
"""

import os
from flask import Flask, request, jsonify
from models import session, User, AuthLog
from uuid import uuid4
from datetime import datetime

app = Flask(__name__)

# Flask Routes
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get("username")
    email = data.get("email")
    password = uuid4().hex  # Generate secure password

    new_user = User(
        username=username,
        password_hash=password,
        email=email,
        date_registered=datetime.utcnow()
    )
    session.add(new_user)
    session.commit()

    return jsonify({"password": password}), 201

@app.route('/auth', methods=['POST'])
def auth():
    data = request.json
    username = data.get("username")
    user = session.query(User).filter_by(username=username).first()

    if not user:
        return jsonify({"error": "Invalid username"}), 404

    # Log authentication attempt
    auth_log = AuthLog(
        request_ip=request.remote_addr,
        user_id=user.id
    )
    session.add(auth_log)
    session.commit()

    return jsonify({"message": "Authenticated"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
