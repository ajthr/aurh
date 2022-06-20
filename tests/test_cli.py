#!/usr/bin/python
# -*- encoding: utf-8 -*-

"""
:Author: Ajith
:Date: 19/06/2022
:Copyright: © 2022, Ajith
:License: MIT
"""
import subprocess

from aurh import __version__


class TestCLI:

    def test_version(self, helpers):
        result = subprocess.run(['aurh', '--version'], capture_output=True)
        assert helpers.check_none(result.stderr)
        assert __version__ in helpers.decode(result.stdout)
