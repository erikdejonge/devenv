#!/usr/bin/env python3
# coding=utf-8
"""
Project markdowntools

Usage:
  mdonelineparachaps [options] <input>

Options:
  -h --help     Show this screen.

author  : rabshakeh (erik@a8.nl)
project : markdowntools
created : 26 Apr 2016 / 17:48
where   : Latitude: 51.957132
          longitude: 4.569601
          https://www.google.nl/maps/place/51.957132,4.569601
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
