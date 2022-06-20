#!/usr/bin/python
# -*- encoding: utf-8 -*-

"""
:Author: Ajith
:Date: 19/06/2022
:Copyright: © 2022, Ajith
:License: MIT
"""


class TestHelpers:

    @staticmethod
    def decode(string):
        return str(string, 'utf-8')

    @staticmethod
    def check_none(err):
        binary_empty_string = b''
        return err is binary_empty_string
