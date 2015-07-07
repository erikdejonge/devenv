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
from consoleprinter import console

def debug(s):

    console(s, fileref=True)

def main():
    """
    main
    """
    input1 = sys.stdin.read()

    # print("\033[90m", input1, "\033[0m")
    input2 = []
    for line in input1.split("\n---\n")[0].split(" "):
        if len(line.strip()) > 0:
            input2.append(line.strip())
    if len(input1.split("\n---\n")[1].split("alias "))> 30:
        print("too many items")

        return

    if len(input1.split("\n---\n")) > 1:
        for line in input1.split("\n---\n")[1].split("alias "):
            if len(line.strip()) > 0:
                newip = []

                if len(input2) > 0:
                    for rem in input2:
                        if rem in line:
                            pass
                        else:
                            newip.append('alias ' + line.strip())

                    for line2 in newip:
                        if "alias " in line2:
                            line = line.split("=")[0].replace("alias ", "").strip()

                        input2.append(line)
                else:
                    line = line.split("=")[0].replace("alias ", "").strip()
                    input2.append(line)



    input2 = [x.strip() for x in list(set(input2))]
    bashprof = open(os.path.join(os.path.expanduser("~"), ".bash_profile")).read()
    input3 = []

    for line in input2:
        for bline in bashprof.split("\n"):
            if bline.startswith("alias ") and line in bline:
                input3.append(bline.split("=")[0].lstrip("alias "))

    for inp3 in input3:
        input2.append(inp3)

    printed = set([":", '\x1b[33m:\x1b[37m\n\x1b[0m'])
    for line in input2:

        result = '\033[33m' + line.split('=')[0].strip().replace(':', '').strip() + ":"
        implementation = line.split('=')

        if len(implementation) > 1:
            implementation = implementation[1].strip().strip('\'')
        else:
            implementation = implementation[0].strip().strip('\'')

        implementation = implementation.replace(";", "\n")

        if not implementation.endswith("\n"):
            implementation += "\n"

        implist = []

        for impitem in implementation.split("\n"):

            if "function " + impitem + "()" in bashprof:
                spbash = bashprof.split("function " + impitem + "()")
                func = ""

                if len(spbash) > 0:
                    spbash = spbash[1].split("}\n")
                    func = "\033[37mfunction " + impitem + "()" + spbash[0].replace("\n\n", "\n") + "}"

                implist.append(func)
            else:
                spbash = bashprof.split("alias " + impitem + "=")

                if len(spbash) > 1:
                    spbash = spbash[1].split("alias")[0].replace("'", "")
                    spbash = '\n'.join([x.strip() for x in spbash.split(';')])
                    implist.append(spbash)
                else:
                    implist.append(impitem.strip())

        implementation = "\n".join(implist)
        result += '\033[37m\n' + implementation.strip() + '\033[0m'
        result = result.replace("alias ", "")
        if result.strip() not in printed:
            #print(str({1:result.strip()}) + "\n")
            print(result.strip()+"\n")
        printed.add(result.strip())

if __name__ == "__main__":
    main()
