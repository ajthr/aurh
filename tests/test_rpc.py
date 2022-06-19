#!/usr/bin/python
# -*- encoding: utf-8 -*-

"""
:Author: Ajith
:Date: 19/06/2022
:Copyright: © 2022, Ajith
:License: MIT
"""
import pytest

from aurh.rpc import RPC


class TestRPC:

    @pytest.fixture()
    def rpc(self):
        return RPC()

    def test_rpc_make_url(self, rpc, helpers):
        url = "https://aur.archlinux.org/rpc?v=5&type=search&by=name&arg=mugshot"
        result = rpc.make_url("mugshot", rpc.find_rpc, rpc.by_name)
        assert result == url
