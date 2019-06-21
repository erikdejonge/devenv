#!/usr/bin/env python3
# coding=utf-8
"""
Project devenv

Usage:
  parse_stale_packages [options] <input>

Options:
  -h --help     Show this screen.

author  : rabshakeh (erik@a8.nl)
project : devenv
created : 16 Jan 2019 / 14:51
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

    s = open(arguments.input).read()

    l = s.split("\n")
    l2 = [x.split("site-packages")[-1] for x in l if len(x.split("site-packages"))>0]
    l3 = [x.split('/') for x in l2]
    l4 = [x[1] for x in l3 if len(x)>1]
    s1 = set(l4)
    print(s1)
    for i in s1:
        mymod = i.split(" ")[0].rstrip(".py").strip()
        if mymod=='num':
            mymod='numpy'
        if "usr"!=mymod:
            print("sudo pip3 uninstall -y "+mymod)
            print("sudo rm -Rf  /usr/lib/python3.7/site-packages/"+i.split(" ")[0])


if __name__ == "__main__":
    main()
