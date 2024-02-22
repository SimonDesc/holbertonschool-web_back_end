#!/usr/bin/env python3
"""
Manage the Session authentication
"""
import uuid
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
