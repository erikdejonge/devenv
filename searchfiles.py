# coding=utf-8
"""
Search directory for a certain string

Usage:
  searchfiles [options] <searchfolder> <extension> <query>

Options:
  -h --help     Show this screen.

author  : rabshakeh (erik@a8.nl)
project : devenv
created : 15-06-15 / 09:51
"""
import os
import pickle

from arguments import Arguments
from consoleprinter import get_safe_string


class IArguments(Arguments):
    """
    IArguments
    """
    def __init__(self, doc):
        """
        __init__
        """
        self.extension = ""
        self.searchfolder = ""
        self.help = False
        self.query = ""
        super().__init__(doc)

    def get_cachename(self):
        """
        get_cachename
        """
        cachename = self.searchfolder + "_" + self.extension
        return get_safe_string(cachename).lower()


def main():
    """
    main
    """
    arguments = IArguments(__doc__)
    cachefolder = os.path.join(os.path.expanduser("~"), ".searchfiles")

    if os.path.exists(cachefolder) and os.path.isfile(cachefolder):
        raise RuntimeError("cachefolder is file: " + str(cachefolder))

    if not os.path.exists(cachefolder):
        os.makedirs(cachefolder, exist_ok=True)

    cachefilename = os.path.join(cachefolder, arguments.get_cachename())
    searchstruct = {}

    if os.path.exists(cachefilename):
        searchstruct = pickle.load(open(cachefilename))

    for root, folders, files in os.walk(arguments.searchfolder):
        for posfile in files:
            possible_test_file_path = os.path.join(root, posfile)
            if possible_test_file_path.endswith(arguments.extension):
                searchstruct[possible_test_file_path] = open(searchstruct).read()


if __name__ == "__main__":
    main()
