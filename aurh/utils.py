#!/usr/bin/python
# -*- encoding: utf-8 -*-

"""
:Author: Ajith
:Date: 18/06/2022
:Copyright: © 2022, Ajith
:License: MIT
"""

import click


class Utils:

    def __init__(self):
        pass

    @staticmethod
    def clone(url, directory=None):
        pass

    @staticmethod
    def get(url):
        pass

    @staticmethod
    def pretty_print_package_list(data, current_page, paginate_by, total):
        start = current_page * paginate_by
        click.clear()
        for index, data in enumerate(data):
            click.secho(" {0} ".format(str(index + start + 1)), nl=False, fg="red")
            click.secho(" {0} ".format(str(data["Name"])), nl=False, fg="blue", bold=True)
            click.secho(" v{0} ".format(str(data["Version"])), nl=False, fg="yellow")
            click.secho(" ({0}) ".format(str(data["Popularity"])), nl=True, fg="cyan")
            click.secho("    {0}".format(str(data["Description"])), nl=True, fg="white")
            click.secho("    {0}".format(str(data["Maintainer"])), nl=True, fg="blue")
            click.secho("")

        click.secho(" ==> Total Packages: {0}".format(total))
        click.secho(" ==> Page {0} of {1}".format(current_page + 1, str(int((total / paginate_by) + 1))), nl=False)
        click.secho("                           [n]ext / [p]revious] ", bold=True, fg="cyan")
        click.secho(" ==> Packages to Install (eg: 1 2 3)", nl=False)
        click.secho("       [q]uit] ", bold=True, fg="red")

    @staticmethod
    def installation_confirmation_prompt(data, args):
        click.secho("These {0} packages will be installed".format(len(args)))
        for _index, index in enumerate(args):
            click.secho(" {0}) {1}".format(_index + 1, data[index - 1]["Name"]))
        return click.confirm("Proceed with installation?", default=True, prompt_suffix="")
