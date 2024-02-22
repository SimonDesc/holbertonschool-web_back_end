#!/usr/bin/env python3
"""
Manage the Basic authentication
"""
from api.v1.auth.auth import Auth
import base64


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
            s = b.decode("utf-8")
            return s
