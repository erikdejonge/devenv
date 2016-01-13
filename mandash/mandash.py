#!/usr/bin/env python3
# coding=utf-8
"""
Lorum ipsum

Usage:
  mandash.py [options] <term1> [<term2>] [<term3>]

Options:
  -h --help     Show this screen.

author  : rabshakeh (erik@a8.nl)
project : devenv
created : 13-01-16 / 11:36
"""
import sys

from cmdssh import cmd_run, shell
from arguments import Arguments
import os
try:
    (width, height) = os.get_terminal_size()
except OSError as ex:
    width = 1100
    height = 1100

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
        self.term1 = ""
        self.term2 = ""
        self.term3 = ""
        super().__init__(doc)
import tempfile


def main():
    """
    main
    """
    arguments = IArguments(__doc__)
    query = arguments.term1

    if arguments.term2:
        query += " " + arguments.term2

    if arguments.term3:
        query += " " + arguments.term3

    with tempfile.NamedTemporaryFile(buffering=False) as tf:
        result = ""
        try:
            result = cmd_run("/usr/bin/man " + query, streamoutput=False, verbose=True)
        except (BaseException) as ex:
            print("opening dash")
            shell("open dash://" + query.replace(" ", ":"))
            return

        tf.write(result.encode('utf-8'))
        tf.seek(0)

        if result.count('\n') > height:
            shell("less " + tf.name)
        else:
            shell("more " + tf.name)


if __name__ == "__main__":
    main()
