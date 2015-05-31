#!/usr/bin/env python3
# coding=utf-8
"""
Start an OSX app

Usage:
  openmacapp.py [options] <name>

Options:
  -h --help     Show this screen.

author  : rabshakeh (erik@a8.nl)
project : devenv
created : 31-05-15 / 11:08
"""
import os
import glob

from arguments import Arguments
from consoleprinter import doinput


class IArguments(Arguments):
    """
    IArguments
    """
    def __init__(self, doc=None):
        """
        @type doc: str, None
        """
        self.help = False
        self.name = ""
        super().__init__(doc)


def main():
    """
    main
    """
    arguments = IArguments(__doc__)
    os.chdir("/Applications")
    applist = []

    for app in glob.glob("*.app"):
        if arguments.name.lower().strip() in app.lower().strip():
            applist.append(app)

    if len(applist) == 1:
        os.system("open /Applications/" + applist[0])
    else:
        answer = doinput(description="Which one?", default="q", answers=applist, force=False, returnnum=True)
        os.system("open '/Applications/" + applist[answer]+"'")


if __name__ == "__main__":
    main()
