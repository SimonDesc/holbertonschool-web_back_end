#!/usr/bin/env python3
"""
Manage the Basic authentication
"""
from typing import TypeVar
from api.v1.auth.auth import Auth
import base64
from models.base import Base
from models.user import User


class BasicAuth(Auth):
    """Basic Auth
    """

    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """ Returns the Base64 part of the Authorization header
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        else:
            return authorization_header[6:]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """  Returns the decoded value of a Base64
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            base64.b64encode(base64.b64decode(
                base64_authorization_header)) == base64_authorization_header
        except Exception:
            return None
        else:
            # Base64 decode the encoded string into bytes.
            b = base64.b64decode(base64_authorization_header)
            # Decode the bytes into str.
            s = b.decode("utf-8", errors='ignore')
            return s

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> (str, str):  # type: ignore
        """ Returns the user email and password from the Base64 decoded value
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        else:
            split_str = decoded_base64_authorization_header.split(":")
            user = split_str[0]
            password = split_str[1]
            return user, password

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> TypeVar('User'):  # type: ignore
        """ Returns the User instance based on his email and password
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None

        if (not users or
                users == [] or
                users is None or
                not users[0].is_valid_password(user_pwd)):
            return None

        return users[0]

    def current_user(self, request=None) -> TypeVar('User'):  # type: ignore
        """ API is fully protected by a Basic Authentication
        """
        authorization_header = self.authorization_header(request)
        base64_authorization_header = self.extract_base64_authorization_header(
            authorization_header)
        decoded_b64_auth_header = self.decode_base64_authorization_header(
            base64_authorization_header)
        user_credentials = self.extract_user_credentials(
            decoded_b64_auth_header)

        user = self.user_object_from_credentials(user_credentials[0],
                                                 user_credentials[1])
        if user is None:
            return None
        return user
