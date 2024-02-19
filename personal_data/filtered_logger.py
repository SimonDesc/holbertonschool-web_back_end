#!/usr/bin/env python3
"""
filter_datum
"""

import re


def filter_datum(fields: list[str], redaction: str, message: str, separator: str) -> str:
    """A function used to obfuscate the log message"""
    for field in fields:
        # Création du motif regex pour trouver le champ et sa valeur
        pattern = re.compile(r'{}=.*?{}'.format(field, separator))
        # Remplacement de chaque occurrence du champ par le champ
        # lui-même et le texte d'offuscation
        message = pattern.sub(f'{field}={redaction}{separator}', message)
    return message
