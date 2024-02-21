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
        """
        Return: False
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Return: None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):  # type: ignore
        """
        Return: None
        """
        return None
