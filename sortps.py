#!/usr/bin/env python3
# coding=utf-8
"""
Reformats ps output (piped)

Usage:
  sortps

Options:
  -h --help     Show this screen.

author  : rabshakeh (erik@a8.nl)
project : devenv
created : 15-06-15 / 15:45
"""
import os
import sys


def main():
    """
    main
    """
    psauxdict = {}
    lines = []
    for line in os.popen("ps aux").read().split("\n"):
        lines.append(line)
    lines.pop(0)
    for line in lines:

        lineparts = [linepart for linepart in line.split(" ") if linepart]
        if len(lineparts) > 0:
            psauxdict[lineparts[1]] = " ".join(lineparts[10:]).split(" ")

    lines = []

    for line in sys.stdin:
        lines.append([linepart for linepart in line.split(" ") if linepart])

    lines.sort(key=lambda linepart:(float(linepart[1]), float(linepart[2]), float(linepart[3])))

    for line in lines:
        #print(line)
        result = '\033[33m' + str(line[1]) + "\t("+line[2]+", "+line[3]+")\t"
        if line[1] in psauxdict:
            proc = " ".join(psauxdict[line[1]]).split(" ")

        else:
            proc = " ".join(line[10:]).split(" ")
        if ".app" in proc[0]:
            proc[0] = proc[0].split(".app")[0]
        
        result += '\033[30m ' + os.path.basename(proc[0])
        if len(proc) > 1:
            result += " "
            result += " ".join(proc[1:])[:80]
            if len(" ".join(proc[1:]))> 80:
                result += "..."
        result += '\033[0m'
        result = result.replace("\n", "").strip()
        print(result)


if __name__ == "__main__":
    main()
