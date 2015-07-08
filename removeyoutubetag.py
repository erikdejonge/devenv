#!/usr/bin/env python3
# coding=utf-8
"""
Print mv commands to remove youtube tags

Usage:
  removeyoutubetag.py [options] <inputdir>

Options:
  -h --help     Show this screen.

author  : rabshakeh (erik@a8.nl)
project : devenv
created : 24-06-15 / 13:49
"""
import os
import time

from arguments import Arguments
from consoleprinter import console, forceascii, console_warning


class IArguments(Arguments):
    """
    IArguments
    """
    def __init__(self, doc):
        """
        __init__
        """
        self.help = False
        self.inputdir = ""
        super().__init__(doc)


def remove_youtube_tag(fpath, root):
    """
    @type fpath: str
    @type root: str
    @return: None
    """
    fpathsplit = os.path.splitext(fpath)
    fpathsplitext = fpathsplit[0].strip()
    fpathsplitextlast = fpathsplit[1]
    splitrev = fpathsplitext.split("-")
    splitrev.reverse()
    taglen = 0
    tag = ""
    nfpath = fpath

    for fpj in splitrev:
        tag = fpj
        taglen = len(fpj)
        break

    if taglen >= 11 and "." in tag:
        for fpk in tag.split("."):
            tag = fpk
            taglen = fpk
            break

    if taglen == 10:
        nfpath = forceascii(fpathsplitext).replace("-" + tag, "").strip("_").strip("-").strip() + fpathsplitextlast
        fpath = os.path.join(root, fpath)
        nfpath = os.path.join(root, nfpath)
    elif taglen == 11:
        if "-" + tag in fpath:
            nfpath = forceascii(fpathsplitext).replace("-" + tag, "").strip("_").strip("-").strip() + fpathsplitextlast
            fpath = os.path.join(root, fpath)
            nfpath = os.path.join(root, nfpath)

    elif fpathsplitext.endswith("_") or fpathsplitext.endswith("-") or fpathsplitext.endswith(" ") or fpathsplitext.startswith("_") or fpathsplitext.startswith("-") or fpathsplitext.startswith(" "):
        nfpath = forceascii(fpathsplitext).strip("_").strip("-").strip() + fpathsplitextlast
        fpath = os.path.join(root, fpath)
        nfpath = os.path.join(root, nfpath)

    return fpath, nfpath


def main():
    """
    main
    """
    arguments = IArguments(__doc__)

    if not os.path.expanduser(arguments.inputdir):
        console(arguments.inputdir)
        console_warning("path does not exist")
        return

    roots = set()

    # for root, _, _ in os.walk(arguments.inputdir):
    #    roots.add(root)
    roots.add(arguments.inputdir)
    print(remove_youtube_tag("ADHD - A case of over diagnosis  - Dr. David A. Sousa at TEDxASB-ygKNRnz7q5o.mp3", ""))
    return
    for root in roots:
        for fpath in os.listdir(root):
            fpath, nfpath = remove_youtube_tag(fpath, root)
            if fpath!=nfpath:
                print("mv", '"' + fpath + '"', '"' + nfpath + '"')


if __name__ == "__main__":
    main()
