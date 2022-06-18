#!/usr/bin/python
# -*- encoding: utf-8 -*-

"""
:Author: Ajith
:Date: 18/06/2022
:Copyright: © 2022, Ajith
:License: MIT
"""

import click

from . import __version__


@click.group()
@click.help_option()
@click.version_option(version=__version__)
def main():
    pass


@main.command(name="find", help="find AUR packages")
@click.argument("package", nargs=-1)
def find(package):
    print(package)


@main.command(name="info", help="get info about AUR packages")
@click.argument("package", nargs=-1)
def info(package):
    print(package)


@main.command(name="clone", help="clone AUR package source from https://aur.archlinux.org/")
@click.argument("package", nargs=-1)
def clone(package):
    print(package)


@main.command(name="install", help="install AUR package(s)")
@click.argument("package", nargs=-1)
def install(package):
    print(package)


@main.command(name="update", help="update AUR package(s)")
@click.argument("package", nargs=-1)
def update(package):
    print(package)


@main.command(name="query", help="query all installed AUR package")
@click.argument("package", nargs=-1)
def query(package):
    print(package)


@main.command(name="remove", help="remove an installed AUR package")
@click.argument("package", nargs=-1)
def remove(package):
    print(package)


if __name__ == '__main__':
    main()
