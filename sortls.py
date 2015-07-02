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
from consoleprinter import console, Colors

def main():
    """
    main
    """
    input = sys.stdin.read()
    for line in input.split("\n"):
        console(line)

if __name__ == "__main__":
    main()
