#!/usr/bin/env python3
"""
filter_datum
"""

import logging
from typing import List
import re


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """A function used to obfuscate the log message"""
    for field in fields:
        message = re.sub(fr'{field}=.+?{separator}',
                         f'{field}={redaction}{separator}',
                         message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: list):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        original_message = super().format(record)
        redacted_message = filter_datum(self.fields,
                                        self.REDACTION,
                                        original_message,
                                        self.SEPARATOR)
        return redacted_message
