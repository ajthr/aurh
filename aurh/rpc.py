#!/usr/bin/python
# -*- encoding: utf-8 -*-

"""
:Author: Ajith
:Date: 18/06/2022
:Copyright: © 2022, Ajith
:License: MIT
"""

import json

import requests

from aurh.exceptions import RepositoryError, NetworkError


class RPC:
    base = "https://aur.archlinux.org"
    rpc = "/rpc?v=5"
    find_rpc = "&type=search"
    info_rpc = "&type=info"
    multiinfo_rpc = "&type=multiinfo"
    by_name = "&by=name"
    by_maintainer = "&by=maintainer"
    by_depends = "&by=depends"
    by_makedepends = "&by=makedepends"

    def __init__(self):
        pass

    def make_url(self, kwd, action_rpc, by_field=None):
        by_field = "" if not by_field else by_field
        arg = "&arg=" + kwd
        return self.base + self.rpc + action_rpc + by_field + arg

    def find(self, kwd, flag=None):

        if flag == 1:
            url = self.make_url(kwd, self.find_rpc, self.by_name)
        elif flag == 2:
            url = self.make_url(kwd, self.find_rpc, self.by_maintainer)
        elif flag == 3:
            url = self.make_url(kwd, self.find_rpc, self.by_depends)
        elif flag == 4:
            url = self.make_url(kwd, self.find_rpc, self.by_makedepends)
        else:
            url = self.make_url(kwd, self.find_rpc)

        try:
            resp = requests.get(url)
            resp.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise NetworkError(str(e))
        data = json.loads(resp.text)
        if data["type"] == "error":
            raise RepositoryError(data["error"])
        return sorted(data["results"], key=lambda d: d["Popularity"], reverse=True)

    def info(self, package):
        pass

    def clone(self, package, directory=None):
        pass
