#!/usr/bin/python
import os
from os import rename, listdir
path = "."
try:
    dirList = listdir(path)
except:
    print 'There was an error while trying to access the directory: '+path
def work(name):
    newname = path+'/'+name.lower().capitalize().replace("_", " ")
    print(name)
    try:
        rename(path+'/'+name, newname)
    except Exception, e:
        print 'Process failed for file: '+name, e
    if os.path.isdir(newname):
        os.chdir(newname)

        for name in listdir("."):
            work(name)
        os.chdir("..")
for name in listdir(path):
    work(name)

