# coding=utf-8
"""
Prints aliasses where query is in alias or implementation

Usage:
  sortalias [options] <query>

Options:
  -h --help     Show this screen.

author  : rabshakeh (erik@a8.nl)
project : devenv
created : 15-06-15 / 15:45
"""
from arguments import Arguments


def main():
    """
    main
    """
    arguments = Arguments(__doc__)
    print(arguments)
    #"alia"s | grep $1
    #['@!@'+x for x in lines]" | puf "['\033[33m'+x.split('=')[0].lstrip('alia'+'s').strip() +':\033[30m\n'+x.split('=')[1].strip('\'')+'\033[0m\n' for x in lines]" | puf "[x for x in lines if x]" | puf "'\\x1b[33m'+''.join(['  '+x.strip()+'\n' for x in '  '.join(lines).strip().split(';') if x]).strip().replace(':', ':\n').strip().replace('@!@', '\n\n').replace('  \\x1b[', '\\x1b[').replace('\n\n\n', '\n\n').replace('\n\x1b[0m\x1b[33m\n\n', '\x1b[0m\x1b[33m\n\n').lstrip('\x1b[33m\n\n')"

if __name__ == "__main__":
    main()
