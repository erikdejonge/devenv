# coding=utf-8
"""
convert rst file

Usage:
  rst2md.py [options] <rstfile>

Options:
  -h --help     Show this screen.
  -c --clean    Remove the rst file if conversion is successful
  -f --force    Overwrite existing md files.
  -v --verbose  Print arguments
  -s --silent   Folder from where to run the command [default: .].
"""
from arguments import Arguments

import os


def main():
    """
    main
    """
    arg = Arguments(doc=__doc__)

    if arg.verbose is True:
        print(arg)

    if not os.path.exists(arg.rstfile):
        print("file does not exist")
        return

    if arg.force is False:
        if os.path.exists(arg.rstfile.replace(".rst", ".md")):
            print("\033[91m" + arg.rstfile.replace(".rst", ".md") + " exists\033[0m")
            return

    if not arg.silent:
        print("\033[94m" + arg.rstfile.lower(), "->\033[0;96m", arg.rstfile.lower().replace(".rst", ".md") + "\033[0m")
    open(arg.rstfile + ".tmp", "w").write(open(arg.rstfile).read().replace(".. auto", "-- auto").replace("   :", "-- :"))
    try:
        os.system("pandoc -f rst -t markdown_github " + arg.rstfile + ".tmp" + " -o " + arg.rstfile.lower().replace(".rst", ".md") + " 2> /dev/null")
        # noinspection PyBroadException
        try:
            codebuf = [x for x in open(arg.rstfile.lower().replace(".rst", ".md"))]
            codebuf.append("")
            cnt = 0
            codebuf2 = ""

            for l in codebuf:
                try:
                    checkword = codebuf[cnt + 1]
                except IndexError:
                    checkword = ""

                if "sourceCode" in l:
                    if "$" in checkword:
                        l = l.replace("sourceCode", "bash")
                    elif ">" in checkword:
                        l = l.replace("sourceCode", "bash")
                    elif "<" in checkword:
                        l = l.replace("sourceCode", "html")
                    else:
                        l = l.replace("sourceCode", "python")

                l = l.replace("*[", "##").replace("]*", "")

                if "-- " in l:
                    l = l.replace("-- a", "\n.. a").strip()
                    l = l.replace("-- :", "\n   :").strip()
                    l = l.replace("\\", "")

                    if ":target: <" in l:
                        l = l.replace(":target: <", "^ [target](").replace(">", ")").replace("^", ">")
                    else:
                        l = "```\n" + l + "\n```"

                codebuf2 += l
                cnt += 1

            open(arg.rstfile.lower().replace(".rst", ".md"), "w").write(codebuf2)
        except:
            codebuf = open(arg.rstfile.lower().replace(".rst", ".md")).read()
            codebuf = codebuf.replace("sourceCode", "python")
            open(arg.rstfile.lower().replace(".rst", ".md"), "w").write(codebuf)

        if arg.clean is True:
            os.remove(arg.rstfile)
    finally:
        os.remove(arg.rstfile + ".tmp")


if __name__ == "__main__":
    main()