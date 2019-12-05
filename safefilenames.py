# coding=utf-8
"""
Project devenv

Usage:
  safefilenames.py [options] <filepath>

Options:
  -d --dryrun   Do not modify files, display commands
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
        self.dryrun = False
        self.seen = set()
        self.recursive = False
        self.filepath = None
        super().__init__(doc)


def ossystem(args, cmd):
    """
    @type args: IArguments
    @type cmd: str
    @return: None
    """
    print(cmd)

    if args.dryrun:
        os.system(cmd)


def change_filepath(arg, fdp, fp):
    """
    @type arg: IArguments
    @type fdp: str
    @type fp: str
    @return: None
    """
    ext = [
        'a',
        'ai',
        'aif',
        'aifc',
        'aiff',
        'au',
        'avi',
        'bat',
        'bcpio',
        'bin',
        'bmp',
        'c',
        'cdf',
        'cpio',
        'csh',
        'css',
        'csv',
        'dat',
        'db',
        'dll',
        'doc',
        'docx',
        'dot',
        'dmg',
        'dng',
        'dvi',
        'eml',
        'eps',
        'epub',
        'etx',
        'exe',
        'flac',
        'gif',
        'gz',
        'gzip',
        'gtar',
        'h',
        'hdf',
        'htm',
        'html',
        'ico',
        'ief',
        'jpe',
        'jpeg',
        'jpg',
        'js',
        'ksh',
        'latex',
        'log',
        'm1v',
        'm3u',
        'm3u8',
        'm4a',
        'm4b',
        'm4v',
        'md',
        'man',
        'me',
        'mht',
        'mobi',
        'mhtml',
        'mif',
        'mkv',
        'mov',
        'movie',
        'mp2',
        'mp3',
        'mp4',
        'mpa',
        'mpe',
        'mpeg',
        'mpg',
        'ms',
        'nc',
        'nws',
        'nvram',
        'o',
        'obj',
        'oda',
        'part',
        'p12',
        'p7c',
        'pbm',
        'pdf',
        'pfx',
        'pgm',
        'pl',
        'png',
        'pnm',
        'pot',
        'ppa',
        'ppm',
        'pps',
        'ppt',
        'pc',
        'ps',
        'pwz',
        'py',
        'pyc',
        'pyo',
        'qt',
        'ra',
        'ram',
        'ras',
        'rdf',
        'rgb',
        'roff',
        'rtf',
        'rtx',
        'sgm',
        'sgml',
        'sh',
        'shar',
        'smc',
        'snd',
        'so',
        'src',
        'srt',
        'sv4cpio',
        'sv4crc',
        'svg',
        'swf',
        't',
        'tar',
        'tcl',
        'tex',
        'texi',
        'texinfo',
        'tif',
        'tiff',
        'tr',
        'tsv',
        'txt',
        'ustar',
        'vcf',
        'vmsd',
        'vmx',
        'vmxf',
        'vmdk',
        'wav',
        'webm',
        'wiz',
        'wsdl',
        'xbm',
        'xlb',
        'xls',
        'xml',
        'xpdl',
        'xpm',
        'xsl',
        'xwd',
        'zip']

    nfp = get_safe_filename_string(fp)

    # print(nfp)

    if nfp == 'ds_store':
        if os.path.exists(nfp):
            os.remove(nfp)
    else:
        for i in ext:
            mext = "." + i

            # print(nfp, mext+mext)

            if nfp.endswith(mext + mext):
                nfp2 = nfp.strip(mext)
                nfp2 += mext
                nfp = nfp2

        if 'ds_store' not in nfp.lower() and 'vhs_emmj_indexed' not in nfp.lower() and 'youtube' not in nfp.lower() and "imovie" not in nfp.lower():
            replaces = ['1080p', 'bluray', 'x264', 'dts-jyk', '1080p', 'brrip', '1080p', '720p', 'lolettv', 'internal', 'hevc-psa', 'fleet', 'killersettv', 'fumettv', 'yts', 'xvid-etrg', 'webrip', 'x264-deflateettv', 'hdtv', 'x264', 'proper', '-deepguy', '1080p', 'bluray', 'x264', 'dts-jyk', '1080p', 'yts', 'multisub', '_ger', 'highcode', '-phd', 'eng_subs', 'h264', '-mp4', 'xvid', 'hdrip', 'x264-killersettv',
                        'x264', 'gaz', 'yify', 'ac3', '1080p', 'etrg', 'brrip', '-evo', '_evo', '720p', '480p', 'bluray', 'web_dl', 'reenc', 'deejayahmed', 'aac', 'team_nanban', 'repack', 'hdtv', 'dvdscr', '.hq', 'hive-cm8', 'hd-ts', 'extended', 'proper', 'cpg', '.hc']

            # replaces.extend([str(x) for x in range(1950, 2020)])
            for i in replaces:
                if "marit" not in i:
                    nfp = nfp.replace(i, "").replace("..", ".").replace("-.", ".").replace("_.", "__").strip(".").strip("_").strip("-").strip(".").replace(".", "-").replace("_nfo", ".txt").replace("_url", ".txt")

            for i in ext:
                e = "_" + i
                n = "." + i
                nfp = nfp.replace(e, n)

        for i in ext:
            e = "_" + i + "." + i
            n = "." + i
            nfp = nfp.replace(e, n)

        for i in ext:
            e = "_" + i
            n = "." + i

            if nfp.endswith(e):
                nfp = nfp.strip(e)
                nfp += n

                # print(nfp)

        nfp = nfp.replace(" ", "_").strip("_")
        nfp = nfp.replace("_-_", "_").strip(".").strip("_")

        for i in range(0, 3):
            nfp = nfp.replace("..", ".").replace("-.", ".").replace("_.", ".").strip(".").strip("_").strip("-").strip(".")

        slist = list(nfp)

        for i in range(0, slist.count(".") - 1):
            slist[slist.index(".")] = "-"

        # for i in range(0,slist.count("-")-1):
        #    slist[slist.index("-")]="_"
        nfp = ''.join(slist)

        # print(nfp.count("-"))
        if 1 == nfp.count("-"):
            nfps = nfp.split("-")

            print(nfps)
            nfpsext = nfps[1].split(".")[-1]
            nfp = nfps[0] + "." + nfpsext

        nfpl = nfp.split(".")
        nfp2 = "_".join(nfpl[:-1])
        nfp2 += "." + nfpl[-1]

        # print(nfp2)
        if fp != nfp:
            if os.path.isdir(fdp):
                ffp = os.path.join(fdp, fp)
                fnfp = os.path.join(fdp, nfp)
            else:
                ffp = fp
                fnfp = nfp

            if os.path.exists(fnfp):
                raise Exception("File exists")

            if ffp != fnfp and not os.path.exists(fnfp):
                print(ffp, "->", fnfp)
                ossystem(arg, 'mv "' + ffp + '" "' + fnfp + '"')


skipmsg = set()


def walkdir(args, recursive, fdp):
    """
    @type args: IArguments
    @type recursive: bool
    @type fdp: str
    @return: None
    """
    global skipmsg
    skipnames = ['$RECYCLE.BIN', '.git', '.gitignore']

    for fp in os.listdir(fdp):
        skip = False

        for skipname in skipnames:
            if skipname in fp:
                skip = True

        if not skip:
            change_filepath(args, fdp, fp)

            if recursive is not None:
                fpd = os.path.join(fdp, fp)

                if os.path.isdir(fpd):
                    walkdir(args, recursive, fpd)
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
        change_filepath(arguments, os.path.dirname(arguments.filepath), os.path.basename(arguments.filepath))
    else:
        for i in range(0, 10):
            walkdir(arguments, arguments.recursive, arguments.filepath)


if __name__ == "__main__":
    main()
