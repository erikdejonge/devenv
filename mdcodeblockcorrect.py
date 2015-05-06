# coding=utf-8
"""
convert rst file

Usage:
  mdcodeblockcorrect.py [options] <mdfile>

Options:
  -h --help     Show this screen.
  -v --verbose  Print arguments
  -s --silent   Folder from where to run the command [default: .].
"""
from arguments import Arguments

import os


def correct_codeblocks(mdfile):
    """
    @type mdfile: str
    @return: None
    """
    inbuf = [x.rstrip().replace("\t", "    ") for x in open(mdfile)]
    outbuf = []
    cb = False
    inblock = False
    cnt = 0

    for l in inbuf:
        if "'''" in l:
            return 0
    for l in inbuf:
        if l.strip().startswith("```"):
            if inblock:
                inblock = False
            else:
                inblock = True

        if not inblock:
            if (l.strip().startswith("sed") or l.strip().startswith("gsed")) and not cb:
                outbuf.append("\n```bash")
                cnt += 1
                cb = True

            elif l.startswith("    ") and not l.strip().startswith("<") and not "/>" in l and not l.endswith(";") and not cb :
                if not cb:
                    cnt += 1
                    outbuf.append("\n```python")

                cb = True
            else:
                if cb is True:
                    if not (l.strip().startswith("sed") or l.strip().startswith("gsed")):
                        cb = False
                        outbuf.append("```\n")

            if cb is True:
                l = l.replace("    ", "", 1)
        # used for sed cheatcheat conversion
        # if l.endswith(":"):
        #     l = "#"+l.lower().capitalize()
        # else:
        #     if l.strip().startswith("# "):
        #         l = l.strip().replace("# ", "").capitalize()
        outbuf.append(l)

    if cb is True:
        outbuf.append("```")

    open(mdfile, "w").write("\n".join(outbuf))
    return cnt


def main():
    """
    main
    """
    arg = Arguments(doc=__doc__)

    if arg.verbose is True:
        print(arg)

    if arg.mdfile.lower().strip().endswith(".markdown"):
        print("mv "+arg.mdfile+" "+arg.mdfile.replace(".markdown", ".md"))
        os.system("mv "+arg.mdfile+" "+arg.mdfile.replace(".markdown", ".md"))
    return
    if not os.path.exists(arg.mdfile):
        print("file does not exist")
        return

    mdfile = arg.mdfile
    cnt = correct_codeblocks(mdfile)

    if not arg.silent:
        if cnt != 0:
            print("\033[94m" + arg.mdfile.lower(), "->\033[0;96m " + str(cnt) + " code blocks corrected\033[0m")


if __name__ == "__main__":
    main()
