#!/usr/bin/env python3
# coding=utf-8
"""
Follow all symbolic link paths, input <cmdpath> can be a command or a path

Usage:
  wwhich.py [options] <cmdpath>

Options:
  -h --help     Show this screen.

author  : rabshakeh (erik@a8.nl)
project : devenv
created : 22-07-15 / 15:20
"""

import os
import sys

from sh import which
from arguments import Arguments
from consoleprinter import console


if sys.version_info.major < 3:
    print("\033[31mPython 3 is required\033[0m")
    exit(1)


class IArguments(Arguments):
    """
    IArguments
    """
    def __init__(self, doc):
        """
        __init__
        """
        self.help = False
        self.cmdpath = ""
        super().__init__(doc)


def main():
    """
    main
    """
    arguments = IArguments(__doc__)
    tracepath = ""

    if os.path.exists(arguments.cmdpath):
        tracepath = arguments.cmdpath
    else:
        tracepath = which(arguments.cmdpath)

    console(tracepath)

if __name__ == "__main__":
    main()

