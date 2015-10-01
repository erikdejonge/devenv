# coding=utf-8
"""
Lorum ipsum

Usage:
  openfile.py [options] <input>

Options:
  -h --help     Show this screen.

author  : rabshakeh (erik@a8.nl)
project : devenv
created : 30-09-15 / 20:57
"""
import sys

from arguments import Arguments
from consoleprinter import console

if sys.version_info.major < 3:
    console("\033[31mpython3 is required\033[0m")
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
