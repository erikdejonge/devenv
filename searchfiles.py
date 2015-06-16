# coding=utf-8
"""
Search directory for a certain string

Usage:
  searchfiles [options] <searchfolder> <extension> <query>

Options:
  -h --help     Show this screen.
  -r --reset    Reset searchcache
  -c --clean    Clean searchcache

author  : rabshakeh (erik@a8.nl)
project : devenv
created : 15-06-15 / 09:51
"""
import os
import pickle

from arguments import Arguments
from consoleprinter import get_safe_string, print_stdout


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
        self.reset = False
        self.clean = False
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
    if arguments.clean is True:
        for filepath in os.listdir(cachefolder):
            print(filepath)
        return
    cachefilename = os.path.join(cachefolder, arguments.get_cachename())
    searchstruct = {}

    if arguments.reset is False and os.path.exists(cachefilename):

        searchstruct = pickle.load(open(cachefilename, "rb"))
        print("\033[34mloading search",len(searchstruct),"\033[0m")
    else:
        print("\033[34mbuilding search\033[0m")

        for root, folders, files in os.walk(arguments.searchfolder):
            if len(searchstruct) % 100 == 0:

            for posfile in files:
                possible_test_file_path = os.path.join(root, posfile)
                #print(arguments.extension.strip(), possible_test_file_path)
                if arguments.extension.strip()=="all" or possible_test_file_path.lower().endswith(arguments.extension.lower()):
                    try:
                        searchstruct[possible_test_file_path] = open(possible_test_file_path).read()
                    except UnicodeDecodeError as ex:
                        searchstruct[possible_test_file_path] = str(ex)
                    except FileNotFoundError as ex:
                        searchstruct[possible_test_file_path] = str(ex)
                    except OSError as ex:
                        searchstruct[possible_test_file_path] = str(ex)
        pickle.dump(searchstruct, open(cachefilename, "wb"))

    for filepath in searchstruct:
        if arguments.query.lower() in searchstruct[filepath].lower():
            print("\033[33m" + filepath + "\033[0m")
            print("\033[37m" + str(os.popen("cat -n '" + filepath + "' | tr '[:upper:]' '[:lower:]' | grep " + arguments.query.lower()).read()) + "\033[0m")


if __name__ == "__main__":
    main()
