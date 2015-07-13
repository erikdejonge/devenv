# coding=utf-8
"""
Convert a file to plain ascii

Usage:
  force_ascii.py [options] <input>

Options:
  -h --help     Show this screen.

author  : rabshakeh (erik@a8.nl)
project : devenv
created : 13-07-15 / 14:21
"""
from arguments import Arguments
from consoleprinter import forceascii


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
    content = open(arguments.input, "rt").read()

    print(content)


if __name__ == "__main__":
    main()
