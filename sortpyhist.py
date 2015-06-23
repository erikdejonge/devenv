# coding=utf-8
"""
Sort python history paths

Usage:
  sortpyhist [options] <input>

Options:
  -h --help     Show this screen.

author  : rabshakeh (erik@a8.nl)
project : devenv
created : 23-06-15 / 08:22
"""
from arguments import Arguments
class IArguments(Arguments):
    """
    IArguments
    """
    def __init__(self, doc):
        """
        __init__
        """
        self.help=False
        self.input=""
        super().__init__(doc)

def main():
    """
    main
    """
    arguments = IArguments(__doc__)
    print(arguments)


if __name__ == "__main__":
    main()
