__author__ = 'dlohani'

'''

The class Mergedir is used to copy all the files in source directory
plus all the files in all of it's source directory to
a single destination directory, hence merge directories



'''

import os
from os import path
import shutil
import filecmp


class Mergedir:
    newnamecount = 0
    def __init__(self):
        return

    def merge(self, sourcedir, destdir):
        # the merging code
        # exit if source does not exist
        if not path.exists(sourcedir) or not path.isdir(sourcedir):
            print("Error the source directory does not exist")
            return
        if not path.exists(destdir) or not path.isdir(destdir):
            print("Error the destination directory does not exist")
            return
        for fpath, subdirs, files in os.walk(sourcedir):
            for filename in files:
                f = path.join(fpath, filename)
                Mergedir.copyfile(self, path.realpath(f), destdir)
        return

    def copyfile(self, sourcefile, destdir):
        filepath, filename = path.split(sourcefile)
        destfile = path.join(destdir,filename)
        if path.exists(destfile):
            print(filename+" file already exists, replacing giving a new name")
            if not filecmp.cmp(sourcefile,destfile):
                # get a new name for destfile
                self.newnamecount += 1
                name, extension = path.splitext(filename)
                newfilename = name + "_" + str(self.newnamecount) + extension
                destfile = path.join(destdir,newfilename)
                print("Both files use same name")
            else:
                #do nothing
                print("Both are same file skipping")
                return
        shutil.copy(sourcefile, destfile)
        return
