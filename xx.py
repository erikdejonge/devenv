#!/usr/bin/env python3
# coding=utf-8
"""
Project xx

Usage:
  xx [options] <input>

Options:
  -h --help     Show this screen.

author  : rabshakeh (erik@a8.nl)
project : xx
created : 21 Jun 2018 / 13:57
where   : [?25l\
          [?25l[1000d[k[1a[1000d[k|
          https://www.google.nl/maps/place/[?25l\
          [?25l[1000d[k[1a[1000d[k|
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
