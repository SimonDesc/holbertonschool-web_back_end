#!/usr/bin/env python3
"""Flask entrypoint"""
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth

AUTH = Auth()

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def greet():
    """Home greeting"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    """Registers users"""
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login():
    """Logs users in"""
    email = request.form.get('email')
    password = request.form.get('password')

    if AUTH.valid_login(email, password) is False:
        abort(401)

    cookie = AUTH.create_session(email)
    res = jsonify({"email": email, "message": "logged in"})
    res.set_cookie("session_id", cookie)

    return res


@app.route('/sessions', methods=['DELETE'])
def logout():
    """Logs users out"""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)

    if user:
        AUTH.destroy_session(user.id)
        return redirect('/')
    abort(403)


@app.route('/profile')
def profile():
    """Gets a user"""
    session_id = request.cookies.get('session_id')

    if session_id is None:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)

    if user:
        return jsonify({'email': user.email})
    abort(403)


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token():
    """Gets a reset password token"""
    email = request.form.get('email')

    try:
        token = AUTH.get_reset_password_token(email)
        return jsonify({'email': email, 'reset_token': token})
    except ValueError:
        abort(403)


@app.route('/reset_password', methods=['PUT'])
def update_password():
    """Updates a user's password"""
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_password = request.form.get('new_password')

    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({'email': email, 'message': 'Password updated'})
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
