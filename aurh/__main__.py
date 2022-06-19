#!/usr/bin/python
# -*- encoding: utf-8 -*-

"""
:Author: Ajith
:Date: 18/06/2022
:Copyright: © 2022, Ajith
:License: MIT
"""

import click

from aurh import __version__
from aurh.rpc import RPC
from aurh.utils import Utils


@click.group()
@click.help_option()
@click.version_option(version=__version__)
def main():
    pass


@main.command(name="find", help="find AUR packages")
@click.option("--name", "find_by", flag_value=1, help="find by package name and description")
@click.option("--maintainer", "find_by", flag_value=2, help="find by package maintainer")
@click.option("--depends", "find_by", flag_value=3, help="find by package maintainer")
@click.option("--makedepends", "find_by", flag_value=4, help="find for packages that makedepend on keywords")
@click.option("--paginate", "paginate_by", default=7, help="number of results shown per page")
@click.argument("kwd", nargs=1)
def find(find_by, paginate_by, kwd):
    try:
        rpc = RPC()
        click.secho("Fetching...", fg="cyan")
        results = rpc.find(kwd, flag=find_by)
        paginated_result = [results[i:i + paginate_by] for i in range(0, len(results), paginate_by)]
        i = 0
        while True:
            Utils.pretty_print_package_list(paginated_result[i], i, paginate_by, len(results))
            inp = click.prompt(" ", prompt_suffix="==>")
            if inp.lower() == 'q':
                break
            elif inp.lower() == 'n':
                i = i + 1 if (i + 1 < len(paginated_result)) else i
            elif inp.lower() == 'p':
                i = i - 1 if (i - 1 >= 0) else i
            else:
                try:
                    package_list = list(map(int, inp.strip().split(" ")))
                    if all(i < len(results) for i in package_list):
                        if Utils.installation_confirmation_prompt(results, package_list):
                            print("Installation!")
                        break
                    raise IndexError
                except ValueError:
                    click.secho("package list should contain numbers only!", fg="red")
                    click.pause(info="Press any key to try again...", err=True)
                except IndexError:
                    click.secho("Package index out of range!", fg="red")
                    click.pause(info="Press any key to try again...", err=True)
    except IndexError:
        click.secho("No results found!", fg="red")


@main.command(name="info", help="get info about AUR packages")
@click.argument("package", nargs=1)
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
