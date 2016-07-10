#!/usr/bin/env python3
# coding=utf-8
"""
Project devenv

Usage:
  safefilenames.py [options] <input>

Options:
  -h --help     Show this screen.

author  : rabshakeh (erik@a8.nl)
project : devenv
created : 10 Jul 2016 / 20:41
where   : Latitude: 51.825385
          longitude: 4.651021
          https://www.google.nl/maps/place/51.825385,4.651021
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

def safe_string():
    echo $@|puf "[consoleprinter.get_safe_string(os.path.basename(x)).replace(' ', '_').replace('-', '_').replace('__', '_').replace('___', '_').replace('..', '.').replace('._', '_').lower().replace('|', '_').replace('\'', '').lower().strip('_') for x in lines]"

def main():
    """
    main
    """
    arguments = IArguments(__doc__)
    console(arguments)


if __name__ == "__main__":
    main()
