#!/usr/bin/env python3
# coding=utf-8
"""
Project devenv

Usage:
  code_wisdom_rss [options] <showcount>

Options:
  -h --help     Show this screen.

author  : rabshakeh (erik@a8.nl)
project : devenv
created : 23 Apr 2018 / 15:09
where   :51.9568,4.582
"""

import sys
import feedparser

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
        self.showcount = ""
        super().__init__(doc)


def main():
    """
    main
    """
    arguments = IArguments(__doc__)
    f = feedparser.parse('http://fetchrss.com/rss/addd5388a93f86a598b4567400897512.xml')

    if f and f.entries and len(f.entries) >= arguments.showcount:
        for i in range(0, arguments.showcount):
            print(f.entries[0].title)
    else:
        print("error", len(f.entries), "entries")


if __name__ == "__main__":
    main()
