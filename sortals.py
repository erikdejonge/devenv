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

from consoleprinter import console, remove_color, console_warning


def debug(s):
    """
    @type s: list
    @return: None
    """
    console(s, fileref=True)


def main():
    """
    main
    """
    input = sys.stdin.read()
    searchfor = input.strip()
    profile = open(os.path.expanduser("~/.bash_profile")).read()
    aliasses = []





    for line in profile.split("\n"):
        if line.startswith("alias "):
            sline = line.split("=", 1)

            if len(sline) > 0:
                alias = sline[0].strip().replace("alias ", "")
                imp = sline[1].strip().strip(":").strip("'")
                aliasses.append((alias, imp))
            else:
                console_warning("cant split this", line)
                raise RuntimeError()

    print(get_alias_and_implementation(aliasses, profile, searchfor))

    return



    if len(input1.split("\n---\n")[1].split("alias ")) > 30:
        print("too many items")
        return

    if len(input1.split("\n---\n")) > 1:
        for line in input1.split("\n---\n")[1].split("alias "):
            if len(line.strip()) > 0:
                newip = []
                input2 = list(set(input2))

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
        linecnt = 0

        for bline in bashprof.split("\n"):
            if bline.startswith("alias ") and line in bline:
                input3.append(bline.split("=")[0].replace("alias ", "") + " -> " + str(linecnt))

            linecnt += 1

    for inp3 in input3:
        input2.append(inp3)

    printed = set([":", '\x1b[33m:\x1b[37m\n\x1b[0m'])
    input2.sort()
    last = ""

    for line in input2:
        if "->" not in line:
            if line.strip().startswith("_"):
                result = '\033[34m' + line.split('=')[0].strip().replace(':', '').strip() + ":"
            else:
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
        if remove_color(line.strip().split("->")[0].strip()).strip() is last.strip():
            print(line)
        if "->" in line:
            last = remove_color(line.strip().split("->")[0].strip())
        elif remove_color(line.strip().split("->")[0].strip()) not in str(printed):
            print(result.strip() + "\n")

        printed.add(remove_color(result.strip().split(" -> ")[0].strip()))


def get_alias_and_implementation(aliasses, profile, searchfor):
    retval = ""
    for alias in aliasses:
        if alias[0].strip().lower() == searchfor.strip().lower():
            imp = alias[1].strip()
            retval += "\033[91m" + alias[0].strip() + ": \033[33m" + imp + "\033[0m"
            if imp.startswith("_"):
                for func in profile.split("function "):
                    if func.startswith(imp):
                        retval += "\033[90mfunction " + func.strip() + "\033[0m\n----\n"
    return retval

if __name__ == "__main__":
    main()
