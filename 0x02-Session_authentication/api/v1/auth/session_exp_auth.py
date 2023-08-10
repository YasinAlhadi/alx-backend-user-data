#!/usr/bin/env python3
"""module for class to manage the session expiration"""
from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """Session Exp Auth class"""

    def __init__(self):
        """constructor"""
        try:
            self.session_duration = int(getenv('SESSION_DURATION'))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id: str = None) -> str:
        """creates a Session ID for a user_id"""
        if user_id is None or type(user_id) != str:
            return None
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        session_dictionary = {
            'user_id': user_id,
            'created_at': datetime.now()
        }
        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns a User ID based on a Session ID"""
        if session_id is None or type(session_id) != str:
            return None
        session_dictionary = self.user_id_by_session_id.get(session_id)
        if session_dictionary is None:
            return None
        if self.session_duration <= 0:
            return session_dictionary.get('user_id')
        created_at = session_dictionary.get('created_at')
        if created_at is None:
            return None
        expired_time = created_at + timedelta(seconds=self.session_duration)
        if expired_time < datetime.now():
            return None
        return session_dictionary.get('user_id')
