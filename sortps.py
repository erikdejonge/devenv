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

    first = True
    for line in sys.stdin:
        if not first and len(line) > 0:
            lines.append([linepart for linepart in line.split(" ") if linepart])
        first = False

    lines.sort(key=lambda linepart:(float(linepart[2]), float(linepart[3]), float(linepart[1])))
    print('\033[34mpid\tcpu/mem\t\t program')
    for line in lines:
        memory = line[3]
        if float(memory) > 5:
            memory = "\033[34m" + str(memory)  + "\033[34m"
        cpu = line[2]
        if float(cpu) > 5:
            cpu = "\033[36m" + str(cpu)  + "\033[34m"

        result = '\033[33m' + str(line[1]) + "\t"+cpu+" \033[33m/ "+memory+"\t"
        if line[1] in psauxdict:
            proc = " ".join(psauxdict[line[1]]).split(" ")
        else:
            proc = " ".join(line[10:]).split(" ")
        binary = None
        if ".app" in proc[0]:
            binary = os.path.basename(proc[0])
            proc[0] = proc[0].split(".app")[0]

        dirname =  os.path.dirname(proc[0])
        if dirname:
            dirname += "/"

        result += '\033[30m ' + str(dirname + os.path.basename(proc[0])).strip()
        if binary:
            result += "/"+binary
        if len(proc) > 1:
            result += " "
            result += " ".join(proc[1:])[:80]
            if len(" ".join(proc[1:]))> 80:
                result += "..."
        result += '\033[0m'
        result = result.replace("\n", "").strip()
        #print(line)
        print(result)


if __name__ == "__main__":
    main()
