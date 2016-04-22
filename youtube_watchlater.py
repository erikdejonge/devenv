#!/usr/bin/env python3
# coding=utf-8
"""
Downloads the watchlater playlist, and converts mp4 to to m4a, it then generates two rss feeds with podcast enclosures
Video podcast: http://<YOURIP>:8000/wl_video_youtube.xml
Audio podcast: http://<YOURIP>:8000/wl_video_youtube.xml

Usage:
  process_youtube.py [options] <command>

Options:
  -h --help     Show this screen.
  -c --clear    Clear cache
  -a --audio    Only audio
  -p --playlist Playlist

Commands:
  download download youtube
  process make audiobooks
  downloadprocess download and process

author  : rabshakeh (erik@a8.nl)
project : research
created : 01-08-15 / 01:25
"""
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
from __future__ import absolute_import
from builtins import int
from builtins import super
from builtins import open
from builtins import str
from future import standard_library
standard_library.install_aliases()
import os
import sys
import glob
import json
import shutil
import hashlib
import datetime
import time
import PyRSS2Gen
import socketserver
import os.path
import http.server
import subprocess

from consoleprinter import console, stty_sane, bar, slugify, clear_screen, query_yes_no
from cmdssh import cmd_exec
from mutagen import mp4
from arguments import Arguments

if sys.version_info.major < 3:
    print("\033[31mPython 3 is required\033[0m")
    exit(1)

G_DEBUG = False
G_DOWNLOAD = "download"
G_DOWNLOADPROCESS = "downloadprocess"
G_PODCAST = "podcast"
G_PROCESS = "process"
G_TRYCNT = 120
G_YOUTUBE_PW = open(os.path.expanduser("~/.ytpw")).read()
G_PLAYLIST = "WL"
G_PLAYLIST_FRIENDLY = "Watch later"
G_FEED_PREFIX = "wl_"
G_IPADDRESS


class IArguments(Arguments):
    """
    IArguments
    """
    def __init__(self, doc):
        """
        __init__
        """
        self.help = False
        self.clear = False
        self.audio = False
        self.download = False
        super().__init__(doc)


def check_extensions(fname, extensions):
    """
    @type fname: str
    @type extensions: list
    @return: None
    """
    for ext in extensions:
        if fname.lower().endswith(ext.lower()):
            return True

    return False


def ensure_folder(fname):
    """
    @type fname: str
    @return: None
    """
    if not os.path.exists(fname):
        os.makedirs(fname)


def get_youtube_tags():
    """
    get_youtube_tags
    """
    if not os.path.exists("youtubetags.tmp.txt"):
        if os.path.exists("playlist.json"):
            outf = open("youtubetags.tmp.txt", "w")
            jsn = open("playlist.json").read().strip()
            jsnl = [jc for jc in jsn.split("\n")]
            for jsni in jsnl:
                jd = json.loads(jsni)
                outf.write(jd["url"] + "\n")
        else:
            console("playlist.json", warning=True)
            os_system("nice -n 10 youtube-dl  https://www.youtube.com/playlist?list=" + G_PLAYLIST + " --username=rabshakeh777@gmail.com --password='" + G_YOUTUBE_PW + "' --flat-playlist -j --yes-playlist > playlist.json ")
            return []

    return [x.strip() for x in open("youtubetags.tmp.txt").read().strip().split("\n")]


def make_command(convert_from, convert_to, cmdlist, cnt, ldr, recognized):
    """
    @type convert_from: str
    @type convert_to: str
    @type cmdlist: list
    @type cnt: int
    @type ldr: list
    @type recognized: list
    @return: None
    """
    flabel = None

    for ival in ldr:
        if ival.lower().endswith(convert_from) and not os.path.isdir(ival) and check_extensions(ival.lower(), recognized):
            orgival = ival
            ival = ival.replace("'", "\'").replace('"', '\"')
            newfilename = make_name(orgival, convert_to)
            timestamp = datetime.datetime.now().strftime("%Y.;%j").replace(";0", "").replace(";", "")
            label = make_name(ival, convert_to).rsplit(".", 1)[0]

            # label = snake_case(camel_case(label.replace("  ", " "))).replace("_", " ")
            cnt += 1
            dlabel = label

            if len(label) > 20:
                mid = "..."
                dlabel = str(cnt) + "> " + label[:18]
                dlabel += mid
                dlabel += label[-16:]

                if len(dlabel) < 20:
                    dlabel += " " * (20 - len(dlabel))

            if flabel is None:
                flabel = dlabel
            label += " ({:0.2f}mb)".format(float(os.path.getsize(orgival)) / 1000 / 1000)
            if not os.path.exists(newfilename):
                newfilenamenotyoutubetag = os.path.basename(ival).replace(convert_from, convert_to).rstrip(convert_to)
                cmd = "ffmpeg -i " + shellquote(orgival) + " -c:a libfdk_aac -f mp4  -threads 4 -thread_type frame -metadata composer='process_youtube.py' -metadata artist='" + \
                      timestamp + "' -metadata genre='Youtube audio' -metadata album='Youtube download' " \
                                  "-metadata title=" + shellquote(newfilenamenotyoutubetag) + " -vn " + shellquote(newfilename)

                cmdlist.append(((dlabel, str(cnt) + "> " + label), cmd, orgival))
            else:
                console("File already there", newfilename)
        else:
            recognized = [convert_to, convert_from, ".py", ".pyc"]

            if os.path.isfile(ival) and not check_extensions(ival, recognized):
                console("Filetype not recognized", ival, color='red')

    return flabel


def make_feed(rootfolder):
    """
    @type rootfolder: str
    @return: None
    """
    try_albumart()
    cwd = os.getcwd()
    os.chdir(os.path.expanduser(rootfolder))

    # #  the url of the folder where the items will be stored
    rssfolder = os.path.expanduser(rootfolder).replace("\\", "/")

    # rss_item_url = rss_site_url + quote(str_url1.encode("utf8"))
    console(rssfolder, color="blue")

    # mp3files = [(x, str(x).split(".")[0]) for x in os.listdir(".") if x.endswith("m4a") and os.path.isfile(x)]
    mp4files = [(x, str(x).split(".")[0]) for x in os.listdir(".") if x.endswith("mp4") and os.path.isfile(x)]

    # feed = feedparser.parse("")
    # eed["feed"]["published"] = format_date(str(datetime.datetime.now()))
    # feed["entries"].append({"title":f[1], "enclosure": f[0]})
    # rss_add_item(G_PLAYLIST_FRIENDLY + " Audio Youtube feed", mp3files, rootfolder, G_FEED_PREFIX + "audio_youtube.xml", "http://www.muhlenberg.edu/images/main/academics/llc/audio-icon-blue_000.jpg")
    rss_add_item(G_PLAYLIST_FRIENDLY + " Video Youtube feed", mp4files, rootfolder, G_FEED_PREFIX + "video_youtube.xml", "http://www.mactrast.com/wp-content/uploads/2015/09/video.png")

    os.chdir(cwd)


def make_name(astr, convert_to):
    """
    @type astr: str
    @type convert_to: str
    @return: None
    """
    return astr.replace(".mp4", convert_to).replace(".m4a", convert_to)


def get_osx_creation_time(filename):
    """Accepts a filename as a string. Gets the OS X creation date/time by parsing "mdls" output.
    Returns file creation date as a float; float is creation date as seconds-since-epoch.
    """
    status, output = subprocess.getstatusoutput('/usr/bin/mdls -name kMDItemFSCreationDate "%s"' % (filename))
    if status != 0:
        print('Error getting OS X metadata for %s. Error was %d. Error text was: <%s>.' %
              (filename, status, output))

        sys.exit(3)

    datestring = output.split('=')[1].strip()
    datestring_split = datestring.split(' ')
    datestr = datestring_split[0]
    timestr = datestring_split[1]

    # At present, we're ignoring timezone.
    date_split = datestr.split('-')
    year = int(date_split[0])
    month = int(date_split[1])
    day = int(date_split[2])
    time_split = timestr.split(':')
    hour = int(time_split[0])
    minute = int(time_split[1])
    second = int(time_split[2])

    # convert to "seconds since epoch" to be compatible with os.path.getctime and os.path.getmtime.
    return time.mktime((year, month, day, hour, minute, second, 0, 0, -1))


def rss_add_item(title, mp3files, rootfolder, rssfile, imageurl):
    """
    @type title: str
    @type mp3files: list
    @type rootfolder: str
    @type rssfile: str
    @type imageurl: str
    @return: None
    """
    items = []

    for f in mp3files:
        try:
            fpath = os.path.expanduser(os.path.join(rootfolder, f[0]))
            fcontent = open(fpath, "rb").read()
            enclosure = PyRSS2Gen.Enclosure("http://" + G_IPADDRESS + ":8000/" + f[0], length=len(fcontent), type="m4a")
            showimgurl = "http://" + G_IPADDRESS + ":8000/" + f[0].replace("m4a", "jpg").replace("mp4", "jpg")
            image = PyRSS2Gen.Image(showimgurl, f[1], showimgurl)
            item = PyRSS2Gen.RSSItem(
                title=f[1].replace("_", " "),
                source=image,
                guid=PyRSS2Gen.Guid(hashlib.md5(str(f[0]).encode()).hexdigest()),
                pubDate=time.ctime(os.path.getctime(fpath)),
                enclosure=enclosure)

            items.append(item)
        except BaseException as be:
            print(be)

            raise

    items = sorted(items, key=lambda x: x.pubDate)
    items.reverse()
    image = PyRSS2Gen.Image(imageurl, "Audio", "http://" + G_IPADDRESS + ":8000/" + rssfile)
    rss = PyRSS2Gen.RSS2(
        title=title,
        link="http://" + G_IPADDRESS + ":8000/" + rssfile,
        description="Youtube downloads",
        lastBuildDate=datetime.datetime.now(),
        items=items,
        image=image
    )
    rss.write_xml(open(rssfile, "w"))


def move_into_place(targetlist):
    """
    @type targetlist: list
    @return: None
    """
    print("\033[30m")

    for target in targetlist:
        cnt = 0

        for name in glob.glob('*'):
            if os.path.isfile(name) and name.lower().endswith(target) and not os.path.exists(os.path.join(target, name)):
                cnt += 1

                # console(os.path.join(target, name)))
                # shutil.copy(name, os.path.join(target, name)))
                os.system("cp -v " + name + " " + os.path.join(target, name))

        console("moved", cnt, target + "s", color="blue")
        print("\033[30m")

    print("\033[0m")


def move_leftovers():
    """
    move_leftovers
    """
    lstdr = os.listdir(".")
    keep = [".mp4", ".mp4", ".m4a", ".py", ".pyc"]
    lstdrt = [fe for fe in lstdr if os.path.isfile(fe) and __file__ not in fe]
    lstdr = []

    for ilstdr in lstdrt:
        add = True

        for ki in keep:
            if ilstdr.endswith(ki):
                add = False

        if add is True:
            lstdr.append(ilstdr)

    if len(lstdr) > 0:
        if not os.path.exists("tmp"):
            os.makedirs("tmp", exist_ok=True)

    for fe in lstdr:
        shutil.move(fe, "tmp")


def move_outof_place(targetlist):
    """
    @type targetlist: list
    @return: None
    """
    for target in targetlist:
        for name in glob.glob('*'):
            if not os.path.exists(os.path.basename(name)):
                shutil.move(os.path.join(target, name), ".")
            else:
                if os.path.exists(os.path.join(target, name)):
                    os.remove(os.path.join(target, name))


def os_system(cmd):
    """
    @type cmd: str
    """
    console(cmd, stack=1, fileref=True)
    os.system(cmd)


def preparefordownload(targetlist):
    """
    @type targetlist: list
    @return: None
    """
    for target in targetlist:
        os.makedirs(target, exist_ok=True)

        for name in glob.glob(target + '/*'):

            # print(name, os.path.exists(os.path.basename(name)))

            if not os.path.exists(os.path.basename(name)):
                shutil.move(name, ".")


def query_fs_make_ffmpeg_cmd():
    """
    query_fs_make_ffmpeg_cmd
    """
    targetlist = ["mp4", "m4a"]
    preparefordownload(targetlist)
    cnt = 0
    cmdlist = []
    os.system("pwd")
    recognized = [".mp4", "m4a"]

    # make_command(".m4a", ".m4a", cmdlist, cnt, ldr.copy(), recognized)
    ldr = [x for x in glob.glob("*.mp4") if os.path.isfile(x) and os.path.getsize(x) != 0]
    flabel = make_command(".mp4", ".m4a", cmdlist, cnt, ldr, recognized)
    return cmdlist, flabel


def shellquote(astr):
    """
    @type astr: str
    @return: None
    """
    return "'" + astr.replace("'", "'\\''") + "'"


def slugify2(astr):
    """
    @type astr: str
    @return: None
    """
    astr = astr.replace("-", "")
    astr = slugify(astr)
    astr = astr.replace("__", "_")

    # astr = camel_case(astr)
    return astr


def start_conversion():
    """
    start_conversion
    """
    trycnt = 0

    # while True:
    # if G_EVENT.isSet():
    #     return
    cmdlist, flabel = query_fs_make_ffmpeg_cmd()

    if len(cmdlist) > 10:
        clear_screen(True)

    console(str(121 - (G_TRYCNT - trycnt)) + ". Active8 audiobookbuilder", plaintext=True, color="orange")

    if len(cmdlist) == 0:
        console("nothing to do.", plaintext=True, color="green")
    else:
        console("convert " + str(len(cmdlist)) + " items.", plaintext=True, color="blue")
        print()
        cmdlist2 = []
        ivals = []
        show_todolist = False

        if len(cmdlist) > 1:
            show_todolist = True

        for cmd in cmdlist:
            if show_todolist:
                console(cmd[0][1], plaintext=True, color="grey")

            cmdlist2.append((cmd[0][0], cmd[1]))
            ivals.append(cmd[2])

        cmdlist = cmdlist2

        if show_todolist:
            print()

        if flabel is None:
            flabel = "None"

        for cmd in bar(cmdlist, label=flabel, expected_size=len(cmdlist)):
            cmdtoprint = None

            if G_DEBUG:
                cmdtoprint = cmd

            code, rv = cmd_exec(cmd, cmdtoprint=cmdtoprint, display=G_DEBUG, myfilter=None)

            # console(cmd)
            if code != 0:
                console(rv[0])

    trycnt += 1


def try_albumart():
    """
    try_albumart
    """
    nl = False
    modified_files = set()

    for mediaf in os.listdir("."):
        if not os.path.isdir(mediaf) and (mediaf.lower().endswith("m4a") or mediaf.lower().endswith("mp4")):
            try:
                img = mediaf.replace("m4a", "jpg").replace("mp4", "jpg")

                if os.path.exists(img):
                    if nl is True:
                        print()
                        nl = False

                    media = mp4.MP4(mediaf)
                    fd = open(img, "rb")

                    # Drop the entire PIL part
                    covr = mp4.MP4Cover(fd.read(), getattr(
                        mp4.MP4Cover,
                        'FORMAT_PNG' if img.endswith('png') else 'FORMAT_JPEG'
                    ))
                    fd.close()  # always a good thing to do

                    # if len(media['covr'][0]) == 0:

                    if 'covr' not in media:
                        modified_files.add(mediaf.split(".")[0].strip())
                        media['covr'] = [covr]  # make sure it's a list
                        media.save()

                else:
                    print(".", end="")
                    nl = True
                    sys.stdout.flush()
            except BaseException as ex:
                console(str(ex), color="red")

    modified_files = list(modified_files)
    modified_files.sort(key=lambda x: len(x))

    for mf in modified_files:
        console("Modified cover art: ", mf)

    print()


def update_cache():
    """
    update_cache
    """
    if not os.path.exists("cache"):
        os.mkdir("cache")

    if len([x for x in os.listdir(".") if x.endswith(".json")]) > 0:
        os_system("cp -n *.json cache/")

    if os.path.exists('cache/playlist.json'):
        os_system("cp -n cache/playlist.json .")

    os_system("cp -n *.mp4 cache/ 2> /dev/null")
    os_system("cp -n *.m4a cache/ 2> /dev/null")
    os_system("cp -n *.jpg cache/ 2> /dev/null")


def main():
    """
    main
    """
    global G_PLAYLIST

    print("\033[91m== Youtube Watch Later ==\033[0m")
    arguments = IArguments(__doc__)

    if arguments.clear is True:
        remove = query_yes_no("Remove?")

        if remove is True:
            os_system("rm -f cache/*.mp4")
            os_system("rm -f cache/*.m4a")
            os_system("rm -f cache/*.jpg")

    if arguments.playlist is not None:
        G_PLAYLIST = arguments.playlist

    if os.path.exists("mp4") and len(os.listdir("mp4")) > 0:
        os_system("cp -nv mp4/* ./cache/&&rm -Rf mp4")

    if os.path.exists("m4a") and len(os.listdir("m4a")) > 0:
        os_system("cp -nv m4a/* ./cache/&&rm -Rf m4a")

    ensure_folder("mp4")
    ensure_folder("m4a")

    if arguments.command.lower() == G_DOWNLOAD or arguments.command.lower() == G_DOWNLOADPROCESS:
        if os.path.exists("cache"):
            os_system("mv -f cache/* .")

        print("\033[90m")
        playlistcmd = "nice -n 10 youtube-dl -q -o '%(title)s' https://www.youtube.com/playlist?list=" + G_PLAYLIST + " --username=rabshakeh777@gmail.com --password='" + G_YOUTUBE_PW + "' --flat-playlist -j --yes-playlist > playlist.json"

        # audiocmd = "nice -n 10 youtube-dl -o '%(title)s.m4a' https://www.youtube.com/playlist?list=" + G_PLAYLIST + " --username=rabshakeh777@gmail.com --password='" + G_YOUTUBE_PW + "' -i  --rm-cache-dir --restrict-filenames --audio-format=best --format=m4a"
        videocmd = "nice -n 10 youtube-dl -o '%(title)s.mp4' https://www.youtube.com/playlist?list=" + G_PLAYLIST + " --username=rabshakeh777@gmail.com --password='" + G_YOUTUBE_PW + "' -i --rm-cache-dir --restrict-filenames --write-info-json  --no-warnings --audio-format=best --write-thumbnail -f 18 --recode-video=mp4"

        if arguments.audio is False:
            playlistcmd += " &"

            # audiocmd += " -q &"

        os_system(playlistcmd)

        if arguments.audio is False:
            os_system(videocmd)

        print("\033[0m")
    try:
        if arguments.command.lower() == G_PROCESS or arguments.command.lower() == G_DOWNLOADPROCESS:
            if os.path.exists(".DS_Store"):
                os_system("mv -f cache/* .")

            # parts = [x for x in os.listdir('.') if x.endswith(".part")]
            parts = []

            if len(parts) > 0:
                console("Partial files found", color='red')
                console(os.getcwd(), color="blue")

                for part in parts:
                    console(" ", " ", part, color="darkyellow")

                remove = query_yes_no("Remove?")

                if remove is True:
                    for part in parts:
                        console("removing", part, color="red")
                        os.remove(part)
                else:
                    return

            if os.path.exists(".DS_Store"):
                os.remove(".DS_Store")

            start_conversion()
            targetlist = ["mp4", "m4a"]
            move_into_place(targetlist)

            # # move_leftovers()
            # while not G_EVENT.is_set():
            #     time.sleep(0.1)

        if arguments.command.lower() == G_PODCAST:
            if os.path.exists("cache"):
                os_system("mv -f cache/* .")

            make_feed("~/Movies/youtube")
            os.chdir(os.path.expanduser("~/Movies/youtube"))
            try:

                # noinspection PyPep8Naming
                PORT = 8000

                # os.system('nginx -c /usr/local/etc/nginx/nginx.conf')
                # input()
                # os.system('killall nginx')
                handler = http.server.SimpleHTTPRequestHandler
                httpd = socketserver.TCPServer(("" + G_IPADDRESS + "", PORT), handler)
                print("serving at port", PORT)
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("bye")

    finally:

        # os.system("killall Finder; sleep 3")
        stty_sane()

        if os.path.exists("youtubetags.tmp.txt"):
            os.remove("youtubetags.tmp.txt")

        update_cache()
        os_system("mv -f *.json cache/")

        if os.path.exists("cache/playlist.json"):
            os_system("mv -f cache/playlist.json .")

        os_system("mv -f *.mp4 cache/ 2> /dev/null")
        os_system("mv -f *.m4a cache/ 2> /dev/null")
        os_system("mv -f *.jpg cache/ 2> /dev/null")
        os_system("rm -f *.xml")
        os_system("rm -f playlist.json")
        os_system("rm -f *.part")


if __name__ == "__main__":
    main()
