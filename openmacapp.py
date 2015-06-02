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


def search_appfolder(filename, searchfolder):
    """
    @type filename: str
    @type searchfolder: str
    @return: None
    """

    print("\033[37msearch: " + searchfolder  + "\033[0m")
    applist = []
    os.chdir(searchfolder)

    for app in glob.glob("*.app"):
        if filename.lower().strip() in app.lower().strip():
            applist.append(app)

    return applist


def main():
    """
    main
    """
    arguments = IArguments(__doc__)

    applist = []
    applist.extend(search_appfolder(arguments.name, "/Applications"))
    applist.extend(search_appfolder(arguments.name, "/Utilities"))

    if len(applist) == 1:
        os.system("open /Applications/" + applist[0])
    else:
        answer = doinput(description="Which one?", default="q", answers=applist, force=False, returnnum=True)
        os.system("open '/Applications/" + applist[answer] + "'")


if __name__ == "__main__":
    main()
