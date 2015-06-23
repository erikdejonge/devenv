# coding=utf-8
"""
Sort python history paths

Usage:
  sortpyhist [options] <input>

Options:
  -h --help     Show this screen.

author  : rabshakeh (erik@a8.nl)
project : devenv
created : 23-06-15 / 08:22
"""
import os
from arguments import Arguments
from consoleprinter import console, console_warning

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
    if os.path.exists(arguments.input):

        cmdlist = open(arguments.input).read()
        cmdlist = {cmd for cmd in cmdlist.split("\n") if len(cmd.strip())>0}
        for cmd in cmdlist:
            console(cmd, color=)
    else:
        console_warning(arguments.input, "file not found")
if __name__ == "__main__":
    main()
