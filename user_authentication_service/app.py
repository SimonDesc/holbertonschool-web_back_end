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


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """
    DELETE /sessions
    Expect form data:
      - session_id: user's session id

    Return:
      - redirect to root page '/'
    """
    user_session_id = request.cookies.get("session_id")

    if not user_session_id:
        abort(403)

    user = AUTH.get_user_from_session_id(user_session_id)
    if not user:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
