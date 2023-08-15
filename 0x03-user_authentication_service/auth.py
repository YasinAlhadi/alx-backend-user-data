#!/usr/bin/env python3
"""Hash password module"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Method that registers a user and returns the User object"""
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
        else:
            raise ValueError(f'User {email} already exists')

    def valid_login(self, email: str, password: str) -> bool:
        """Method that checks if a user exists and validates the password"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        else:
            return bcrypt.checkpw(password.encode(), user.hashed_password)

    def _generate_uuid(self) -> str:
        """Method that returns a string representation of a new UUID"""
        return str(uuid.uuid4())

    def create_session(self, email: str) -> str:
        """Method that returns the session ID as a string"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        else:
            session_id = self._generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id


def _hash_password(password: str) -> bytes:
    """Hash password function"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
