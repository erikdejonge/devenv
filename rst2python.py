# coding=utf-8
"""
convert rst file

Usage:
  tests.py [options] <rstfile>

Options:
  -h --help     Show this screen.
  -f --force    Overwrite existing md files.
  -s --silent   Folder from where to run the command [default: .].
"""
from arguments import Arguments

import os


def main():
    """
    main
    """
    arg = Arguments(doc=__doc__)

    if not os.path.exists(arg.rstfile):
        print("file does not exist")
        return

    if arg.force is False:
        if os.path.exists(arg.rstfile.replace(".rst", ".md")):
            print("\033[91m" + arg.rstfile.replace(".rst", ".md") + " exists\033[0m")
            return

    if not arg.silent:
        print("\033[94m" + arg.rstfile.lower(), "->\033[0;96m", arg.rstfile.lower().replace(".rst", ".md") + "\033[0m")

    os.system("pandoc -f rst -t markdown_github " + arg.rstfile + " -o " + arg.rstfile.lower().replace(".rst", ".md") + " 2> /dev/null")
    try:
        codebuf = [x for x in open(arg.rstfile.lower().replace(".rst", ".md"))]
        codebuf.append("")
        codebuf.append("")
        codebuf.append("")
        codebuf.append("")
        cnt = 0
        codebuf2 = ""

        for l in codebuf:
            if "sourceCode" in l:
                checkword = codebuf[cnt + 1]

                if "$" in checkword:
                    l = l.replace("sourceCode", "bash")
                elif ">" in checkword:
                    l = l.replace("sourceCode", "bash")
                elif "<" in checkword:
                    l = l.replace("sourceCode", "html")
                else:
                    l = l.replace("sourceCode", "python")

            codebuf2 += l
            cnt += 1

        open(arg.rstfile.lower().replace(".rst", ".md"), "w").write(codebuf2)
    except:
        codebuf = open(arg.rstfile.lower().replace(".rst", ".md")).read()
        codebuf = codebuf.replace("sourceCode", "python")
        open(arg.rstfile.lower().replace(".rst", ".md", "w")).write(codebuf)


if __name__ == "__main__":
    main()
