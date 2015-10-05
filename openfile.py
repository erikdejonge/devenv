#!/usr/bin/env python3
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
import os
import sys
import time

from arguments import Arguments
from consoleprinter import console, query_yes_no

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


def ossystem(cmd):
    """
    @type cmd: str
    @return: None
    """
    #print(cmd)
    os.system(cmd)


def main():
    """
    main
    """
    arguments = IArguments(__doc__)
    print(arguments.input)

    arguments.input = os.path.abspath(os.path.expanduser(str(arguments.input)))

    if not os.path.exists(arguments.input):
        console(arguments.input, "not found", color="red")
        alts = os.popen("mdfind "+os.path.basename(arguments.input)+" | grep "+os.path.basename(arguments.input)+" | grep -v pyc").read()
        alts = str(alts).split("\n")
        if len(alts) > 0:
            for alternative in alts:
                if query_yes_no("Try \033[34m"+alternative+"\033[96m instead?"):
                    arguments.input = alternative
                    break
            else:
                return
        else:
            return
    console("opening", arguments.input, color="darkyellow")
    pycharm = False
    if arguments.input.lower().endswith("py"):
        pycharm = True
        arguments.input = os.path.dirname(arguments.input)
    if os.path.isdir(arguments.input):
        if os.path.exists(os.path.join(arguments.input, ".idea")):
            pycharm = True

    if pycharm:

        ossystem("cd " + os.path.dirname(arguments.input) + "&&/Applications/PyCharm.app/Contents/MacOS/pycharm " + arguments.input + " > /dev/null 2> /dev/null")
        time.sleep(0.2)

        ossystem("osascript -e 'tell application \"Pycharm\" to activate'")
    else:
        os.system("cd " + os.path.dirname(arguments.input) + "&&/usr/bin/open " + arguments.input)

# print(cmd)


if __name__ == "__main__":
    main()
