#!/usr/bin/env python3
# coding=utf-8
"""
Project htmltools

Usage:
  printlinks [options] <input>

Options:
  -h --help     Show this screen.

author  : rabshakeh (erik@a8.nl)
project : htmltools
created : 11 Jan 2017 / 14:30
where   : Latitude: 51.957234
          longitude: 4.569595
          https://www.google.nl/maps/place/51.957234,4.569595
"""
import sys

from arguments import Arguments
from consoleprinter import console
from bs4 import BeautifulSoup
import urllib.request

if sys.version_info.major < 3:
    console("Python 3 is required", color="red", plaintext="True")
    exit(1)


class IArguments(Arguments):
    """
    IArguments
    """

    def __init__(self, doc):
        """
        __init__
        """
        self.help = False
        self.input = ""
        super().__init__(doc)


def main():
    """
    main
    """
    arguments = IArguments(__doc__)
    #console(arguments)

    try:
        resp = urllib.request.urlopen(arguments.input)
        resp = urllib.request.urlopen(arguments.input)
        soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'))
    except ValueError:
        resp = open(arguments.input).read()
        soup = BeautifulSoup(resp,  "html.parser")


    for link in soup.find_all('a', href=True):
        print(link.text)
        print(link['href'].strip(), "\n\n")

if __name__ == "__main__":
    main()
