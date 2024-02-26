#!/usr/bin/env python3
"""Auth module
"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """Hash a password"""
    byte_obj = bytes(password, 'utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(byte_obj, salt)
