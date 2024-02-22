#!/usr/bin/env python3
"""
Manage the Session authentication
"""
import os
import uuid
from models.user import User
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """ Session Authentification
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Create a new session ID for a user id
        """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        else:
            session_id = uuid.uuid4()
            session_id_str = str(session_id)
            self.user_id_by_session_id[session_id_str] = user_id
            return session_id_str

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Returns a User ID based on a Session ID
        """
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ Get current_user by Session ID
        """
        # Valeur du cookie de session
        session_cookie = self.session_cookie(request)
        if session_cookie is None:
            return None
        # 'ID de l'utilisateur à partir de la valeur du cookie
        user_id = self.user_id_for_session_id(session_cookie)
        if user_id is None:
            return None

        return User.get(user_id)

    def destroy_session(self, request=None):
        """ Destroy the session
        Returns :
            - True if suceed
            - False otherwise
        """
        if request is None:
            return False
        # Valeur du cookie de session
        session_cookie = self.session_cookie(request)
        if session_cookie is None:
            return False
        # 'ID de l'utilisateur à partir de la valeur du cookie
        user_id = self.user_id_for_session_id(session_cookie)
        if user_id is None:
            return False

        del self.user_id_by_session_id[session_cookie]
        return True
