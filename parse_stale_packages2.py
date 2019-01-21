#!/usr/bin/env python3
# coding=utf-8
"""
Project devenv

Usage:
  parse_stale_packages2 [options] <input>

Options:
  -h --help     Show this screen.

author  : rabshakeh (erik@a8.nl)
project : devenv
created : 16 Jan 2019 / 14:52
where   : 51° 53' 44" N,4° 33' 31" E

"""
import sys

from arguments import Arguments
from consoleprinter import console

if sys.version_info.major < 3:
    console("Python 3 is required", color="red", plaintext="True")
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
        self.input = ""
        super().__init__(doc)


def main():
    """
    main
    """
    arguments = IArguments(__doc__)
    console(arguments)


if __name__ == "__main__":
    main()
