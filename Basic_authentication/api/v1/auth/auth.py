#!/usr/bin/env python3
""" DocDocDocDocDocDoc
"""
from typing import List, TypeVar
from flask import request


class Auth():
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

    def current_user(self, request=None) -> TypeVar('User'): # type: ignore
        """
        Return: None
        """
        return None
