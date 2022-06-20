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


class TestRPCCommon:

    @pytest.fixture()
    def rpc(self):
        return RPC()

    def test_rpc_make_url_default(self, rpc, helpers):
        url = "https://aur.archlinux.org/rpc?v=5&type=search&arg=dropbox"
        result = rpc.make_url("dropbox", rpc.find_rpc)
        assert result == url

    def test_rpc_make_url_name(self, rpc, helpers):
        url = "https://aur.archlinux.org/rpc?v=5&type=search&by=name&arg=dropbox"
        result = rpc.make_url("dropbox", rpc.find_rpc, rpc.by_name)
        assert result == url

    def test_rpc_make_url_maintainer(self, rpc, helpers):
        url = "https://aur.archlinux.org/rpc?v=5&type=search&by=maintainer&arg=mtorromeo"
        result = rpc.make_url("mtorromeo", rpc.find_rpc, rpc.by_maintainer)
        assert result == url

    def test_rpc_make_url_depends(self, rpc, helpers):
        url = "https://aur.archlinux.org/rpc?v=5&type=search&by=depends&arg=dbus"
        result = rpc.make_url("dbus", rpc.find_rpc, rpc.by_depends)
        assert result == url

    def test_rpc_make_url_makedepends(self, rpc, helpers):
        url = "https://aur.archlinux.org/rpc?v=5&type=search&by=makedepends&arg=gendesk"
        result = rpc.make_url("gendesk", rpc.find_rpc, rpc.by_makedepends)
        assert result == url


class TestRPCFind:

    expected = {
        'Description': 'A free service that lets you bring your photos, docs, and videos anywhere and share them '
                       'easily.',
        'FirstSubmitted': 1232634085,
        'ID': 1097005,
        'LastModified': 1654963630,
        'Maintainer': 'mtorromeo',
        'Name': 'dropbox',
        'NumVotes': 2371,
        'OutOfDate': None,
        'PackageBase': 'dropbox',
        'PackageBaseID': 23363,
        'Popularity': 5.631523,
        'URL': 'https://www.dropbox.com',
        'URLPath': '/cgit/aur.git/snapshot/dropbox.tar.gz',
        'Version': '150.4.5000-1'
    }

    @pytest.fixture()
    def rpc(self):
        return RPC()

    def test_rpc_find_default(self, rpc, helpers):
        kwd = 'dropbox'
        result = rpc.find(kwd=kwd)
        assert self.expected in result

    def test_rpc_find_name(self, rpc, helpers):
        kwd = 'dropbox'
        result = rpc.find(kwd=kwd, flag=1)
        assert self.expected in result

    def test_rpc_find_maintainer(self, rpc, helpers):
        kwd = 'mtorromeo'
        result = rpc.find(kwd=kwd, flag=2)
        assert self.expected in result

    def test_rpc_find_depends(self, rpc, helpers):
        kwd = 'dbus'
        result = rpc.find(kwd=kwd, flag=3)
        assert self.expected in result

    def test_rpc_find_makedepends(self, rpc, helpers):
        kwd = 'gendesk'
        result = rpc.find(kwd=kwd, flag=4)
        assert self.expected in result
