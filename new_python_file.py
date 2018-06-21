# coding=utf-8
"""
Project dev env

Usage:
  $new_python_file [options] <projectname> <filename>

Options:
  -h --help     Show this screen.


author  : rabshakeh (erik@a8.nl)
project : $dev env
created : 26 Apr 2016 / 04:Apr
where   :

"""

import sys


from arguments import Arguments
from consoleprinter import console

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
        self.projectnaam = ""
        self.filenaam = ""

        super().__init__(doc)


def main():
    """
    main
    """

    templ = """#!/usr/bin/env python3\n# coding=utf-8
\"\"\"
Project {PROJECT_NAME}

Usage:
  {NAME} [options] <input>

Options:
  -h --help     Show this screen.

author  : {USER} (erik@a8.nl)
project : {PROJECT_NAME}
created : {DATE} / {TIME}
where   : {WHEREAMI}
\"\"\"
import sys

from arguments import Arguments
from consoleprinter import console

if sys.version_info.major < 3:
    console(\"Python 3 is required\", color=\"red\", plaintext=\"True\")
    exit(1)\n\n
class IArguments(Arguments):
    \"\"\"
    IArguments
    \"\"\"

    def __init__(self, doc):
        \"\"\"
        __init__
        \"\"\"
        self.help = False
        self.input = \"\"
        super().__init__(doc)\n\n
def main():
    \"\"\"
    main
    \"\"\"
    arguments = IArguments(__doc__)
    console(arguments)\n\n
if __name__ == \"__main__\":
    main()
"""
    import time
    from sh import whoami, whereami
    arguments = IArguments(__doc__)

    project_name = arguments.projectname
    name = arguments.filename
    user = whoami().wait().strip()
    whereamisplit = whereami.stdin.readlines()
    whereamisplit  = whereamisplit.strip().split('\n')
    print(whereamisplit)
    if len(whereamisplit) > 0:
        whereamisplit = whereamisplit[:2]
        whereami = whereamisplit[0]+'\n'
        whereami += '\n'.join([(10*' ')+x for x in whereamisplit[1:]]).lower()+"\n"
        s = whereami.strip().lower().replace("latitude", "").replace("longitude", "")
        s = ','.join([x.strip() for x in s.lower().replace("latitude", "").replace("longitude", "").split(":") if x.strip()])
        whereami += (10*' ')+"https://www.google.nl/maps/place/"+s
    else:
        whereami = "location not available"
    localtime = time.localtime(time.time())
    date = time.strftime("%d %b %Y", localtime)
    time = time.strftime("%H:%M", localtime)
    template_filled = templ.format(PROJECT_NAME=project_name, NAME=name, USER=user, DATE=date, TIME=time, WHEREAMI=whereami)
    #print(template_filled)
    filename = arguments.filename
    if not filename.endswith('.py'):
        filename += ".py"
    open(filename, "w").write(template_filled)


if __name__ == "__main__":
    main()


