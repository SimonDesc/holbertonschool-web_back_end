#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None
AUTH_TYPE = os.getenv('AUTH_TYPE')

if AUTH_TYPE:
    if AUTH_TYPE == 'basic_auth':
        from api.v1.auth.basic_auth import BasicAuth
        auth = BasicAuth()
    elif AUTH_TYPE == 'session_auth':
        from api.v1.auth.session_auth import SessionAuth
        auth = SessionAuth()
    else:
        from api.v1.auth.auth import Auth
        auth = Auth()


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Unauthorized
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Forbidden
    """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def load_user():
    """ Filtering each request. """
    excluded_paths = ['/api/v1/status/',
                      '/api/v1/unauthorized/',
                      '/api/v1/forbidden/',
                      '/api/v1/auth_session/login/']

    if auth is None or not auth.require_auth(request.path, excluded_paths):
        return

    # Si ni l'en-tête d'autorisation ni le cookie de session
    # ne sont présents, refuser l'accès.
    if auth.authorization_header(request) is None \
            and auth.session_cookie(request) is None:
        abort(401)

    # Après avoir confirmé qu'une forme d'authentification est présente,
    # vérifier si un utilisateur courant peut être identifié.
    if auth.current_user(request) is None:
        abort(403)

    # Si un utilisateur est identifié, attribuer cet utilisateur
    # à la requête pour une utilisation ultérieure
    request.current_user = auth.current_user(request)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
