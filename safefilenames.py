#!/usr/bin/env python3
# coding=utf-8
"""
Project devenv

Usage:
  safefilenames.py [options] <filepath>

Options:
  -h --help     Show this screen.

author  : rabshakeh (erik@a8.nl)
project : devenv
created : 10 Jul 2016 / 20:41
where   : Latitude: 51.825385
          longitude: 4.651021
          https://www.google.nl/maps/place/51.825385,4.651021
"""
import os
import sys

from arguments import Arguments
from consoleprinter import console, get_safe_filename_string

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
    for fp in os.listdir(arguments.filepath):
        nfp = get_safe_filename_string(fp)
        if fp != nfp:
            ffp = os.path.join(arguments.filepath, fp)
            fnfp = os.path.join(arguments.filepath, nfp)
            print(fp, "->", nfp)
            os.system('mv "'+ffp+'" "'+fnfp+'"')


if __name__ == "__main__":
    main()

