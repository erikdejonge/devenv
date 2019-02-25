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
    whereamis = None
    c = whereami()
    try:
        whereamis = ''.join([x for x in c.split("[")[-2].strip() if x.isdigit() or x == ',' or x == '.'])

        if whereamis:
            whereamis += "\n" + (10 * ' ') + "https://www.google.nl/maps/place/" + whereami
    except IndexError:
        whereamis = str(whereami())
    finally:
        if not whereamis:
            whereamis = "location not available"

    localtime = time.localtime(time.time())
    date = time.strftime("%d %b %Y", localtime)
    time = time.strftime("%H:%M", localtime)
    template_filled = templ.format(PROJECT_NAME=project_name, NAME=name, USER=user, DATE=date, TIME=time, WHEREAMI=whereamis)

    # print(template_filled)
    filename = arguments.filename

    if not filename.endswith('.py'):
        filename += ".py"

    open(filename, "w").write(template_filled)


if __name__ == "__main__":
    main()
