#!/usr/bin/env python3
# coding=utf-8
"""

Reformats aliasses (piped)

Usage:
  sortalias

Options:
  -h help     Show this screen.

author  : rabshakeh (erik@a8.nl)
project : devenv
created : 15-06-15 / 15:45
"""
import os
import sys

from consoleprinter import console
from consoleprinter import console_warning
from terminaltables import AsciiTable


def debug(s):
    """
    @type s: list
    @return: None
    """
    console(s, fileref=True)


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def get_alias_and_implementation(aliasses, profile, searchfor):
    """
    @type aliasses: list
    @type profile: str
    @type searchfor: str
    @return: None
    """
    retval = ""
    for alias in aliasses:
        if searchfor.strip().lower() in alias[0].strip().lower() or searchfor.strip().lower() in alias[1].strip().lower():
            imp = alias[1].strip()

            if imp.count(";") > 1:
                retval += "\033[30malias " + alias[0].strip() + "=" + imp.strip() + "\"\n"
<<<<<<< HEAD
                retval += "\033[91m" + alias[0].strip() + ":\033[33m\n   " + imp.replace(";", ";\n  ") + "\033[0m\n\n"
            else:
                retval += "\033[91malias " + alias[0].strip() + "=\"\033[33m" + imp + "\033[0m\"\n\n"
=======
                retval += "\033[91m" + alias[0].strip() + ":\033[33m\n   " + imp.replace(";", ";\n  ") + "\033[0m\n---\n"
            else:
                retval += "\033[91malias " + alias[0].strip() + "=\"\033[33m" + imp + "\033[0m\"\n---\n"
>>>>>>> b6e11e4df6fff8e17b08c25f36b014ad34249310

            if imp.startswith("_"):
                foundfunc = False

                for func in profile.split("function "):
                    if func.startswith(imp):
                        foundfunc = True
                        retval += "\033[90mfunction " + func.strip() + "\033[0m\n\n"

                if foundfunc:
<<<<<<< HEAD
                    retval = retval.strip() + "\n\n"
=======
                    retval = retval.strip() + "\n--\n"
>>>>>>> b6e11e4df6fff8e17b08c25f36b014ad34249310

    return retval


def print_finds(aliasses, lines, profile, searchfor):
    """
    @type aliasses: list
    @type lines: list
    @type profile: str
    @type searchfor: str
    @return: None
    """
    retval = get_alias_and_implementation(aliasses, profile, searchfor)

    if len(retval) == 0:
        printing = False

        if searchfor.startswith("_"):
            searchfor = '_'.join(searchfor.split("_")[1:])
        for line in lines:
            if line.strip().startswith("function "):
                if searchfor.lower() in line.lower():
                    printing = True
<<<<<<< HEAD
                    print("\033[0m\033[90m")
=======
                    print("\033[0m--\033[90m")
>>>>>>> b6e11e4df6fff8e17b08c25f36b014ad34249310

            if printing:
                if line.startswith("function"):
                    linesp = line.split("function ")
                    print("function\033[33m", ''.join(linesp[1:]), "\033[90m")
                else:
                    print(line)

            if line.strip().startswith("}"):
                printing = False

                # print("\033[0m")

        if len(retval) == 0:
            cnt = 0

            for line in lines:
                cnt += 1

                if searchfor.lower() in line.lower():
                    if cnt > 3:
                        for i in range(cnt - 3, cnt + 3):
                            if len(lines[i].strip()) > 0:
                                retval += "\033[30m" + str(cnt) + ": \033[33m" + lines[i] + "\n"

                    retval += "\n"

            print(retval)

<<<<<<< HEAD
        print("\033[0m")
=======
        print("--\033[0m")
>>>>>>> b6e11e4df6fff8e17b08c25f36b014ad34249310
    else:
        print(retval)


def no_finds(aliasses):
    """
    @type aliasses: list
    @return: None
    """
    aliasses2 = [x[0] for x in aliasses]
    numcols = 7
    aliaschunks = list(chunks(aliasses2, int(len(aliasses) / numcols)))
    extra = [x[0] for x in aliasses[int(len(aliasses) / numcols) * numcols:]]
    myaliasses = zip(aliaschunks)
    myaliasses2 = []

    for i in myaliasses:
        myaliasses2.append(i[0])

    iline4 = len(myaliasses2[numcols - 1])
    while iline4 < len(myaliasses2[0]):
        myaliasses2[numcols - 1].append(' ')

    lex = len(extra)
    while lex < len(myaliasses2[0]):
        extra.append(' ')
        lex = len(extra)

    zipparam = []

    for i in range(0, numcols):
        zipparam.append(myaliasses2[i])

    zipparam.append(extra)
    zipparam = tuple(zipparam)

    # myaliasses3 = zip(myaliasses2[0], myaliasses2[1], myaliasses2[2], myaliasses2[3], myaliasses2[4], myaliasses2[5], myaliasses2[6], extra)
    myaliasses3 = zip(*zipparam)
    header = ['alias commands']
    header.extend(' ' * numcols)
    myaliasses4 = [header]

    for i in myaliasses3:
        myaliasses4.append(list(i))

    table = AsciiTable(myaliasses4)
    print(table.table)


def main():
    """
    main
    """
    userinput = sys.stdin.read()
    searchfor = userinput.strip()
<<<<<<< HEAD
    profile = str(open(os.path.expanduser("~/.bash_profile"), 'rt').read())
=======
    if os.path.exists(os.path.expanduser("~/.bash_profile")):
        profile = str(open(os.path.expanduser("~/.bash_profile"), 'rt').read())
    if os.path.exists(os.path.expanduser("~/.extend.bashrc")):
        profile += str(open(os.path.expanduser("~/.extend.bashrc"), 'rt').read())

>>>>>>> b6e11e4df6fff8e17b08c25f36b014ad34249310

    # if len(profile.strip()):
    #    profile = profile.encode("utf8")
    aliasses = []
    lines = []

    if len(searchfor) == 0:
        print("possible commands:")

    profile = str(profile)

    for line in profile.split("\n"):
        print(line)
        lines.append(line)
        if line.startswith("alias "):
            sline = line.split("=", 1)
<<<<<<< HEAD

=======
            print(sline)
>>>>>>> b6e11e4df6fff8e17b08c25f36b014ad34249310
            if len(sline) > 0:
                alias = sline[0].strip().replace("alias ", "")
                imp = sline[1].strip().strip(":").strip("'")
                aliasses.append((alias, imp))
            else:
                console_warning("cant split this", line)

                raise RuntimeError()

    # print(len(searchfor), len(aliasses))

    if len(searchfor) == 0:
        no_finds(aliasses)
    else:
        print_finds(aliasses, lines, profile, searchfor)


if __name__ == "__main__":
    main()
