#!/usr/bin/env python3
""" Module of Sessions Authentication views
"""
import os
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def authenticate() -> str:
    """Authenticate users using session auth"""
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or email == '':
        return jsonify({"error": "email missing"}), 400
    if not password or password == '':
        return jsonify({"error": "password missing"}), 400

    users = User.search({'email': email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    SESSION_NAME = os.getenv('SESSION_NAME', 'default_session_name')

    out = jsonify(user.to_json())
    out.set_cookie(SESSION_NAME, session_id)

    return out


@app_views.route('/auth_session/logout',
                 methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """Logout, destroy the session !
    """
    from api.v1.app import auth
    if not auth.destroy_session(request):
        abort(404)
    return jsonify({}), 200
