#!/usr/bin/env python3
# coding=utf-8
"""
Reformats aliasses (piped)

Usage:
  sortalias

Options:
  -h --help     Show this screen.

author  : rabshakeh (erik@a8.nl)
project : devenv
created : 15-06-15 / 15:45
"""
import os
import sys
import subprocess

def main():
    """
    main
    """
    lines = []

    for line in sys.stdin:
        result = '\033[33m' + line.split('=')[0].strip().replace(':', '').strip()
        implementation = line.split('=')[1].strip().strip('\'')
        implementation = implementation.replace(";", "\n")

        if not implementation.endswith("\n"):
            implementation += "\n"

        implist = []

        for impitem in implementation.split("\n"):

            if impitem.startswith("_"):
                bashprof = open(os.path.join(os.path.expanduser("~"), ".bash_profile")).read()
                spbash = bashprof.split(impitem)
                func = ""
                if len(spbash) > 0:
                    spbash = spbash[1].split("}")
                    func = "function "+impitem+spbash[0]+"}\n"
                implist.append(impitem.strip()+": \n"+func)
            else:
                implist.append(impitem.strip())

        implementation = "\n".join(implist)
        result += '\033[90m\n' + implementation + '\033[0m'
        result = result.replace("alias ", "")
        print(result)


if __name__ == "__main__":
    main()
