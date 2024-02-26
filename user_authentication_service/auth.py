#!/usr/bin/env python3
"""Auth module
"""

import uuid
from db import DB
import bcrypt
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError


def _hash_password(password: str) -> bytes:
    """Hash a password"""
    byte_obj = bytes(password, 'utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(byte_obj, salt)


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registrer a new user"""
        exists = True
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            exists = False

        if exists:
            raise ValueError(f'User {email} already exists.')

        return self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        """Credentials validation"""
        exists = True
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            exists = False

        if exists:
            byte_obj = bytes(password, 'utf-8')
            if bcrypt.checkpw(byte_obj, user.hashed_password):
                return True

        return False

    def _generate_uuid(self):
        """Method to generate UUIDs"""
        return str(uuid.uuid4())
