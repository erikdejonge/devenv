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


def get_alias_and_implementation(aliasses, profile, searchfor):
    retval = ""
    for alias in aliasses:
        if alias[0].strip().lower() == searchfor.strip().lower():
            imp = alias[1].strip()
            retval += "\033[91malias " + alias[0].strip() + "=\"\033[33m" + imp + "\033[0m\""
            if imp.startswith("_"):
                for func in profile.split("function "):
                    if func.startswith(imp):
                        retval += "\n\033[90mfunction " + func.strip() + "\033[0m\n----\n"
    return retval

if __name__ == "__main__":
    main()
