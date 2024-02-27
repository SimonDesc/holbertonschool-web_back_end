#!/usr/bin/env python3
"""Auth module
"""

from typing import Union
from uuid import uuid4
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


def _generate_uuid() -> str:
    """Generates a uuid"""
    return str(uuid4())


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

    def create_session(self, email: str) -> str:
        """Return the session ID"""
        try:
            user = self._db.find_user_by(email=email)
        except (InvalidRequestError, NoResultFound):
            return

        uuid = _generate_uuid()
        self._db.update_user(user.id, session_id=uuid)

        return uuid

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """Return the corresponding User or None"""
        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

        return user

    def destroy_session(self, user_id: int) -> None:
        """Delete the session id of a user"""
        self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """Method to reset a password
        Return a string
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError

        uuid = _generate_uuid()
        self._db.update_user(user.id, reset_token=uuid)
        return uuid

    def update_password(self, reset_token: str, password: str) -> None:
        """Updates a user's password"""
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError

        hashed_password = _hash_password(password)
        self._db.update_user(
            user.id, hashed_password=hashed_password, reset_token=None)
