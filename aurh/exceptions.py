#!/usr/bin/python
# -*- encoding: utf-8 -*-

"""
:Author: Ajith
:Date: 18/06/2022
:Copyright: © 2022, Ajith
:License: MIT
"""


class BaseError(Exception):
    """There was an ambiguous error that occurred."""

    def __init__(self, msg, exception_name):
        self.msg = msg
        self.exception_name = exception_name

    def __str__(self):
        return "{0}: {1}".format(self.exception_name, self.msg)


class RepositoryError(BaseError):
    """AUR related errors."""

    exception_name = "RepositoryError"

    def __init__(self, msg):
        super().__init__(msg, self.exception_name)


class NetworkError(BaseError):
    """Various network errors."""

    exception_name = "NetworkError"

    def __init__(self, msg):
        super().__init__(msg, self.exception_name)
