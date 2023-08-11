#!/usr/bin/env python3
"""module for class to manage the API authentication"""
from api.v1.auth.session_exp_auth import SessionAuth
from models.user_session import UserSession
from datetime import datetime


class SessionDBAuth(SessionAuth):
    """Session DB Auth class"""

    def create_session(self, user_id: str = None) -> str:
        """creates a Session ID for a user_id"""
        if user_id is None or type(user_id) != str:
            return None
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        user_session = UserSession(user_id=user_id, session_id=session_id)
        user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns a User ID based on a Session ID"""
        if session_id is None or type(session_id) != str:
            return None
        user_session = UserSession.search({'session_id': session_id})
        if not user_session:
            return None
        user_session = user_session[0]
        if self.session_duration <= 0:
            return user_session.user_id
        if user_session.created_at + self.session_duration < datetime.now():
            return None
        return user_session.user_id

    def destroy_session(self, request=None):
        """deletes the user session / logout"""
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        user_session = UserSession.search({'session_id': session_id})
        if not user_session:
            return False
        user_session = user_session[0]
        try:
            user_session.remove()
            return True
        except Exception:
            return False
