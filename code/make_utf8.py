#!/usr/bin/env python3
# coding=utf-8
"""
Convert a file to plain ascii

Usage:
  make_utf8.py [options] <input>

Options:
  -h --help     Show this screen.

author  : rabshakeh (erik@a8.nl)
project : devenv
created : 13-07-15 / 14:21
"""
import os
import shutil
from arguments import Arguments
from consoleprinter import console


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
    encoding = "utf-8"

    if not os.path.exists("fileencoding.txt"):
        console("no file [fileencoding.txt] found")
        exit(1)
    else:
        encoding = open("fileencoding.txt").read().strip()

    if not os.path.exists(arguments.input):
        console("no file [" + arguments.input + "] found")
        exit(1)
    shutil.copy(arguments.input, arguments.input+".bak")
    content = open(arguments.input+".bak", "rt", encoding=encoding).read()
    content = content.encode("utf-8")
    open(arguments.input+".bak", "wt", encoding="utf-8").write(content.decode())


if __name__ == "__main__":
    main()
