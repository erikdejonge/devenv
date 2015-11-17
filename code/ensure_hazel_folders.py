#!/usr/bin/env python3
# coding=utf-8
"""
Make var/new/github on desktop

Usage:
  ensure_hazel_folders.py

Options:
  -h --help     Show this screen.

author  : rabshakeh (erik@a8.nl)
project : devenv
created : 02-07-15 / 16:22
"""
import os


def new_desktop_folder(foldername):
    """
    @type foldername: str
    @return: None
    """
    folderpath = os.path.join(os.path.expanduser("~"), "Desktop")
    folderpath = os.path.join(folderpath, foldername)

    if not os.path.exists(folderpath):
        os.mkdir(folderpath)


def main():
    """
    main
    """
    new_desktop_folder("new")
    new_desktop_folder("github")
    new_desktop_folder("var")


if __name__ == "__main__":
    main()
