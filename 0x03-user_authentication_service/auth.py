#!/usr/bin/env python3
"""Hash password module"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hash password function"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
