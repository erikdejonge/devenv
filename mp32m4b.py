#!/usr/bin/env python3
# coding=utf-8
"""
Lorum ipsum

Usage:
  mp32m4b.py [options] <input>

Options:
  -h --help     Show this screen.

author  : rabshakeh (erik@a8.nl)
project : devenv
created : 24-06-15 / 13:14
"""
import os
import string
import datetime

from arguments import Arguments
from consoleprinter import console, camel_case, forceascii, console_warning


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


def make_name(astr):
    """
    @type astr: str
    @return: None
    """
    scap = ""

    for word in astr.split():
        scap += word.capitalize() + " "

    astr = scap
    astr = forceascii(astr)

    if "." in astr:
        astr = "".join(astr.rsplit(".", 1)[:-1])

    astr2 = ""
    forb = [".", "-", "_", "@", ",", "'", '"']

    for achar in astr:
        if achar not in forb:
            if achar in string.ascii_letters or achar in string.digits:
                astr2 += achar

    if len(astr2) > 80:
        astr3 = astr2[:40]
        astr4 = astr2[-40:]
    else:
        astr3 = astr2[:int(len(astr2) / 2)]
        astr4 = astr2[int(len(astr2) / 2):]

    astr = camel_case(astr3 + astr4)
    return astr


def shellquote(astr):
    """
    @type astr: str
    @return: None
    """
    return "'" + astr.replace("'", "'\\''") + "'"


def main():
    """
    main
    """
    arguments = IArguments(__doc__)

    if not os.path.expanduser(arguments.input):
        console(arguments.input)
        console_warning("path does not exist")
        return

    ival = arguments.input
    newfilename = make_name(ival) + ".m4a"
    audiobookfilename = make_name(ival) + ".m4b"
    timestamp = datetime.datetime.now().strftime("%Y.;%j").replace(";0", "").replace(";", "")
    cmd = "ffmpeg -i " + shellquote(ival) + " -threads auto -thread_type frame -metadata composer='convertm4b.py' -metadata artist='" + \
        timestamp + "' -metadata album='" + os.path.basename(str(ival)).rsplit(".", 1)[0].replace("'", "").replace("  ", " ") + \
        " Youtube download' -metadata title='" + os.path.basename(str(ival)).rsplit(".", 1)[0].replace("'", "").replace("  ", " ") + \
        "' -vn " + shellquote(newfilename) + "&&mv " + shellquote(newfilename) + " ./Converted&&cd Converted&&mv " + shellquote(newfilename) + " " + shellquote(audiobookfilename)

    print(cmd)


if __name__ == "__main__":
    main()
