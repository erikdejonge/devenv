#!/usr/bin/env python3
# coding=utf-8
"""
Project devenv

Usage:
  safefilenames.py [options] <filepath>

Options:
  -h --help      Show this screen.
  -r --recursive Recursive

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
        self.seen = set()


def change_filepath(fdp, fp):
    """
    @type arguments: IArguments
    @type fp: str
    @return: None
    """
    nfp = get_safe_filename_string(fp)
    if fp != nfp:
        if os.path.isdir(fdp):
            ffp = os.path.join(fdp, fp)
            fnfp = os.path.join(fdp, nfp)
        else:
            ffp = fp
            fnfp = nfp
        if ffp != fnfp:
            print(ffp, "->", fnfp)
            os.system('mv "'+ffp+'" "'+fnfp+'"')


def walkdir(recursive, fdp):
    """
    @type arguments: IArguments
    @return: None
    """

    for fp in os.listdir(fdp):
        change_filepath(fdp, fp)
        if recursive is not None:
            fpd = os.path.join(fdp, fp)

            if os.path.isdir(fpd):
                walkdir(recursive, fpd)


def main():
    """
    main
    """
    arguments = IArguments(__doc__)


    if os.path.isfile(arguments.filepath):
        change_filepath(os.path.dirname(arguments.filepath), os.path.basename(arguments.filepath))
    else:
        for i in range(0,10):
            walkdir(arguments.recursive, arguments.filepath)


if __name__ == "__main__":
    main()
