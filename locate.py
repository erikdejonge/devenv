#!/usr/bin/env python3
# coding=utf-8
"""
Call mdfind to do a quick search

Usage:
  locate.py [options] <query>...

Options:
  -h --help       Show this screen.
  -f --folders    Show folders seperately

author  : rabshakeh (erik@a8.nl)
project : devenv
created : 09-06-15 / 09:35
"""

from __future__ import division, print_function, absolute_import, unicode_literals
from future import standard_library
import os

from arguments import Arguments
from functools import cmp_to_key
from fuzzywuzzy import fuzz
from past.builtins import cmp


class IArguments(Arguments):
    """
    IArguments
    """
    def __init__(self, doc):
        """
        __init__
        """
        self.help = False
        self.folders = False
        self.query = ""
        super().__init__(doc)


def locatequery(args):
    """
    @type args: tuple
    @return: None
    """
    numargs = len(args.query)
    searchword = " ".join(args.query)
    query_display = ", ".join(args.query)
    mdfind_results = []
    textsearch = False

    if searchword.strip().endswith("*"):
        searchword = searchword.strip().strip("*")
        textsearch = True
    elif searchword.strip().endswith("+"):
        searchword = searchword.strip().strip("+")
        textsearch = True

    print("\033[91m[" + query_display + "](" + str(numargs) + "):\033[0m")
    mdfind_results.extend(os.popen("mdfind -onlyin '" + os.path.expanduser("~") + "' -name '" + searchword + "'").read().split("\n"))
    mdfind_results = [x for x in mdfind_results if x]
    mdfind_results.extend(os.popen("mdfind -name '" + searchword + "'").read().split("\n"))

    if textsearch:
        mdfind_results.extend(os.popen("mdfind -onlyin ~/workspace " + searchword).read().split("\n"))

    return mdfind_results, searchword


def show_folders(folders, mdfind_results3, searchword, skiplist):
    """
    @type folders: list
    @type mdfind_results3: str
    @type searchword: str
    @type skiplist: list
    @return: None
    """
    folders2 = []

    if len(folders) > 0 and len(mdfind_results3) < 50:
        print()
        print("\033[91m[" + searchword + "] Folders:\033[0m")
        last = None
        nextcnt = 0

        for i in folders:
            nextcnt += 1
            skip = False
            skipi = i.lower()
            nexti = None
            try:
                nexti = folders[nextcnt]
            except IndexError:
                pass

            for item in skiplist:
                item = item.lower()

                if item in skipi:
                    skip = True

            if last and fuzz.ratio(i, last) > 85:
                skip = True

            if len(folders) < 10:
                skip = False

            if not skip:
                # if last and (pp(i) == pp(last) or fuzz.ratio(i, nexti) > 70):
                #    folders2.append("\033[90m" + str(i) + "\033[0m")
                # else:
                newi = ""

                if nexti:
                    if fuzz.ratio(i, nexti) > 90:
                        newi = "\033[90m" + str(os.path.dirname(i)) + "\033[34m/" + str(os.path.basename(i)) + "\033[0m"

                if newi == "":
                    newi = "\033[34m" + str(i) + "\033[0m"

                folders2.append(newi)

    folders2.sort(key=lambda x: (x.count("/"), len(x), x))
    folders2.reverse()

    for i in folders2:
        print(i)


def main():
    """
    main
    """
    args = IArguments(__doc__)
    mdfind_results, searchword = locatequery(args)
    mdfind_results = [x for x in mdfind_results if x]
    mdfind_results = set(mdfind_results)
    mdfind_results = [xs for xs in mdfind_results if xs]
    mdfind_results2 = []
    folders = []
    skiplist = ["Library/Caches"]
    mdfind_results.sort(key=lambda x: (x.count("/"), len(x), x))

    for i in mdfind_results:
        skip = False
        skipi = i.lower()

        for item in skiplist:
            item = item.lower()

            if item in skipi:
                skip = True

        if not skip:
            mdfind_results2.append(i)

    last = None

    def grandparentpath(apath):
        """
        @type p: str
        @return: None
        """
        return os.path.dirname(os.path.dirname(apath))

    mdfind_results2 = sorted(mdfind_results2, key=cmp_to_key(lambda x, y: cmp(len(y), len(x))))
    mdfind_results2.reverse()
    mdfind_results3 = []

    for i in mdfind_results2:
        if last and (grandparentpath(i) == grandparentpath(last) or fuzz.ratio(i, last) > 70):
            mdfind_results3.append("\033[90m" + str(i) + "\033[0m")
        else:
            mdfind_results3.append("\033[34m" + str(os.path.dirname(i)) + "\033[34m/" + str(os.path.basename(i)) + "\033[0m")

        if os.path.isfile(i):
            folders.append(os.path.dirname(i))
        else:
            folders.append(i)

        last = i

    mdfind_results3.reverse()

    for i in mdfind_results3:
        print(i)

    folders = sorted(set(folders))
    skiplist = ["Library/Mail"]
    folders.sort(key=lambda x: (x.count("/"), len(x), x))

    if args.folders is True:
        show_folders(folders, mdfind_results3, searchword, skiplist)


standard_library.install_aliases()

# sys.stdout.write("\n== current working dir results ==\n\n")
# localdir = os.getcwd()
# for i in [x for x in mdfind_results2 if localdir in x]:

#    sys.stdout.write(i + "\n")

# sys.stdout.flush()

if __name__ == "__main__":
    main()

