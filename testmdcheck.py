# coding=utf-8
"""
devenv/testmdcheck
-
Active8 (07-05-15)
author: erik@a8.nl 
license: GNU-GPL2
"""
import shutil

def main():
    """
    main
    """
    shutil.copy2("./test/bronrst.txt", "./test/testfile.rst")



if __name__ == "__main__":
    main()
    