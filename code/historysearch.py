#!/usr/bin/env python3
# coding=utf-8
"""
Project devenv

Usage:
  historysearch.py [options] <keyword> <historyfile>

Options:
  -h --help     Show this screen.
  -b --bare     Clean commands
  -v --verbose  Verbose

author  : rabshakeh (erik@a8.nl)
project : devenv
created : 02 Nov 2016 / 12:33
where   : Latitude: 51.957135
          longitude: 4.569462
          https://www.google.nl/maps/place/51.957135,4.569462
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
        self.bare = False
        self.verbose = False
        self.historyfile = ""
        self.keyword = ""
        super().__init__(doc)


def main():
    """
    main
    """
    arguments = IArguments(__doc__)
    console(arguments)
    if arguments.verbose:
        console(arguments)
    hs = open(arguments.historyfile).read()
    l = [x.strip().split(' ') for x in hs.split("\n")]
    l2 = [" ".join(x[2:]) for x in l if len(x) > 1]
    l3 = sorted(set(l2))
    ospacers = len(str(len(l3)))
    cnt = 0
    for line in l3:
        spacers = ospacers
        if arguments.keyword in line:
            spacers = spacers - len(str(cnt))
            if arguments.bare:
                print(line)
            else:
                print("\033[34m"+ spacers*' ', cnt ,"\033[33m", line ,"\033[0m")

        cnt += 1

if __name__ == "__main__":
    main()
