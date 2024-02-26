#!/usr/bin/env python3
"""App module
"""
from flask import Flask, jsonify, request, abort, make_response, redirect
from sqlalchemy.orm.exc import NoResultFound
from auth import Auth
app = Flask(__name__)

AUTH = Auth()


@app.route('/', methods=['GET'])
def greet():
    """Welcome route
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    """Users route
    """
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login():
    """Login route
    """
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        if AUTH.valid_login(email, password):
            session_id = AUTH.create_session(email)
            response = jsonify({"email": email, "message": "logged in"})
            response.set_cookie('session_id', session_id)
            return response
        else:
            abort(401)
    except ValueError:
        abort(401)


@app.route('/sessions', methods=['DELETE'])
def logout():
    """Logout route
    """
    id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(id)

    if user:
        AUTH.destroy_session(user.id)
        return redirect('/')
    else:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
