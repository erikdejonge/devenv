# coding=utf-8
"""
Recursively generate an index of all the files in the specified folder

Usage:
  genindex.py [options] <folder> <extension>

Options:
  -h --help     Show this screen.

author  : rabshakeh (erik@a8.nl)
project : devenv
created : 19-05-15 / 15:12
"""
from arguments import Arguments


def main():
    """
    main
    """
    arguments = Arguments(__doc__)
    print(arguments)




if __name__ == "__main__":
    main()
