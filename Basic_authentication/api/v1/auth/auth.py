#!/usr/bin/env python3
""" Manage the API authentication
"""
from typing import List, TypeVar
from flask import request


class Auth():
    """
    Class to manage the authentication
    to the API
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Define which routes don't need authentication
        Return:
            - True if it require auth
            - False otherwise
        """

        if path is None:
            return True
        if path[-1] != '/':
            path += '/'
        if excluded_paths is None or '':
            return True
        if path not in excluded_paths:
            return True
        if path in excluded_paths:
            return False

    def authorization_header(self, request=None) -> str:
        """
        Extract the Authorization header from a request.
        Return :
            - The value of the Authorization header if present, None otherwise.
        """

        if request is None:
            return None
        auth_header = request.headers.get('Authorization')
        return auth_header

    def current_user(self, request=None) -> TypeVar('User'):  # type: ignore
        """
        Return: None
        """
        return None
