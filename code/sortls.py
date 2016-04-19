# coding=utf-8
"""
Sort ls output

Usage:
  someprogram.stdout | sortls

author  : rabshakeh (erik@a8.nl)
project : devenv
created : 02-07-15 / 09:54
"""
import sys
import consoleprinter
def main():
    """
    main
    """
    input = sys.stdin.read()

    for line in input.split("\n"):
        print({1:line})
        linesplit = line.split("  ")
        buf = ""
        cnt = 0
        for lp in linesplit:
            if cnt==3:
                buf += consoleprinter.humansize(str(lp))
            else:
                buf += lp
            cnt += 1
            buf += " "
        print(buf)
        #if len(linesplit) > 5:
        #    print(linesplit[6]+"\n")
            

if __name__ == "__main__":
    main()
