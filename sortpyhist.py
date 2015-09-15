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
import time

from arguments import Arguments
from consoleprinter import console, console_warning, Colors


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
    try:
        arguments = IArguments(__doc__)

        if os.path.exists(arguments.input):
            cmdlist = open(arguments.input).read()
            cmdlist = [cmd for cmd in cmdlist.split("\n") if len(cmd.strip()) > 0 and "sortpyhist.py" not in cmd]

            if 0 == (len(cmdlist)):
                console("the list is empty", color=Colors.red)

            last = ""

            for cmd in cmdlist:
                cmd = cmd.split(": ")

                if len(cmd) > 0:
                    date = cmd.pop(0)
                    date = time.strftime("%Y/%m/%d %H:%M", time.localtime(int(date)))
                    cmd = "".join(cmd)
                    if cmd != last:
                        last = cmd
                        cmd = cmd.replace(os.path.expanduser("~"), "~")

                        if "'" not in cmd and '"' not in cmd:
                            cmd = [cmdi for cmdi in cmd.split("3 ") if cmdi]
                            cmd = " ".join(cmd)
                            cmd = [cmdi for cmdi in cmd.split(" ") if cmdi]
                            cmds = ""

                            for cnt, cmdi in list(enumerate(cmd)):
                                if cnt % 2 == 0:
                                    cmds += "\033[90m"
                                else:
                                    cmds += "\033[93m"

                                cmds += cmdi + " "

                            cmds = cmds.strip()

                        cmd = cmds
                        console(date, cmd, color=Colors.blue)
        else:
            console_warning(arguments.input, "file not found")
    finally:
        print("\033[0m")


if __name__ == "__main__":
    main()

