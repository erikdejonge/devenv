
# coding=utf-8
"""
Project devenv

Usage:
  safefilenames.py [options] <filepath>

Options:
  -h --help      Show this screen.
  -r --recursive Recursive

author  : rabshakeh (erik@a8.nl)
project : devenv
created : 10 Jul 2016 / 20:41
where   : Latitude: 51.825385
          longitude: 4.651021
          https://www.google.nl/maps/place/51.825385,4.651021
"""
import os
import sys

from arguments import Arguments
from consoleprinter import console
from consoleprinter import get_safe_filename_string

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
        self.input = ""
        super().__init__(doc)
        self.seen = set()


def change_filepath(fdp, fp):
    """
    @type arguments: IArguments
    @type fp: str
    @return: None
    """
    ext = ['a', 'ai', 'aif', 'aifc', 'aiff', 'au', 'avi', 'bat', 'bcpio', 'bin', 'bmp', 'c', 'cdf', 'cpio', 'csh', 'css', 'csv', 'dll', 'doc', 'docx', 'dot', 'dvi', 'eml', 'eps', 'etx', 'exe', 'gif', 'gtar', 'h', 'hdf', 'htm', 'html', 'ico', 'ief', 'jpe', 'jpeg', 'jpg', 'js', 'ksh', 'latex', 'm1v', 'm3u', 'm3u8', 'm4v', 'man', 'me', 'mht', 'mhtml', 'mif', 'mkv', 'mov', 'movie', 'mp2', 'mp3', 'mp4', 'mpa', 'mpe', 'mpeg', 'mpg', 'ms', 'nc', 'nws', 'o', 'obj', 'oda', 'p12', 'p7c', 'pbm', 'pdf', 'pfx', 'pgm', 'pl', 'png', 'pnm', 'pot', 'ppa', 'ppm', 'pps', 'ppt', 'ps', 'pwz', 'py', 'pyc', 'pyo', 'qt', 'ra', 'ram', 'ras', 'rdf', 'rgb', 'roff', 'rtf', 'rtx', 'sgm', 'sgml', 'sh', 'shar', 'snd', 'so', 'src', 'srt', 'sv4cpio', 'sv4crc', 'svg', 'swf', 't', 'tar', 'tcl', 'tex', 'texi', 'texinfo', 'tif', 'tiff', 'tr', 'tsv', 'txt', 'ustar', 'vcf', 'wav', 'webm', 'wiz', 'wsdl', 'xbm', 'xlb', 'xls', 'xml', 'xpdl', 'xpm', 'xsl', 'xwd', 'zip']
    nfp = get_safe_filename_string(fp)
    if os.getcwd().endswith("MyMovies") and 'ds_store' not in nfp.lower() and 'youtube' not in nfp.lower() and "imovie" not in nfp.lower():

        replaces = ['multisub', '_ger', 'highcode', '-phd', 'eng_subs', 'h264', '-mp4', 'xvid', 'hdrip', 'x264-killersettv', 'x264', 'gaz','yify','ac3', '1080p', 'etrg', 'brrip', '-evo', '_evo', '720p', '480p', 'bluray', 'web_dl', 'reenc', 'deejayahmed', 'aac', 'team_nanban', 'repack', 'hdtv', 'dvdscr', '.hq', 'hive-cm8', 'hd-ts', 'extended', 'proper', 'cpg', '.hc']
        replaces.extend([str(x) for x in range(1950, 2020)])
        for i in replaces:
            nfp = nfp.replace(i, "").replace("..", ".").replace("-.", ".").replace("_.", "__").strip(".").strip("_").strip("-").strip(".").replace(".", "_").replace("_nfo", ".txt").replace("_url", ".txt")

        for i in ext:
            e = "_"+i
            n = "."+i
            nfp = nfp.replace(e, n)

    for i in ext:
        e = "_"+i+"."+i
        n = "."+i
        nfp = nfp.replace(e, n)
    for i in ext:
        e = "_"+i
        n = "."+i
        if nfp.endswith(e):
            nfp = nfp.strip(e)
            nfp += n
    nfp = nfp.replace("_-_", "_").strip(".").strip("_")
    for i in range(0,3):
        nfp = nfp.replace("..", ".").replace("-.", ".").replace("_.", ".").strip(".").strip("_").strip("-").strip(".")

    if fp != nfp:
        if os.path.isdir(fdp):
            ffp = os.path.join(fdp, fp)
            fnfp = os.path.join(fdp, nfp)
        else:
            ffp = fp
            fnfp = nfp
        if ffp != fnfp:
            print(ffp, "->", fnfp)
            os.system('mv "'+ffp+'" "'+fnfp+'"')

skipmsg = set()
def walkdir(recursive, fdp):
    """
    @type arguments: IArguments
    @return: None
    """
    global skipmsg
    skipnames = ['$RECYCLE.BIN']

    for fp in os.listdir(fdp):
        skip = False
        for skipname in skipnames:
            if skipname in fp:
                skip = True
        if not skip:
            change_filepath(fdp, fp)
            if recursive is not None:
                fpd = os.path.join(fdp, fp)

                if os.path.isdir(fpd):
                    walkdir(recursive, fpd)
        else:
            if fp not in skipmsg:
                print("\033[33mskipping {}\033[0m".format(fp))
                skipmsg.add(fp)

def main():
    """
    main
    """
    arguments = IArguments(__doc__)


    if os.path.isfile(arguments.filepath):
        change_filepath(os.path.dirname(arguments.filepath), os.path.basename(arguments.filepath))
    else:
        for i in range(0,10):
            walkdir(arguments.recursive, arguments.filepath)


if __name__ == "__main__":
    main()
