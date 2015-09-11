__author__ = 'dlohani'

import sys
import mergedir

print(len(sys.argv))
if len(sys.argv) == 3:
    sourcedir = sys.argv[1]
    destdir = sys.argv[2]
    m = mergedir.Mergedir()
    m.merge(sourcedir,destdir)
else:
    print('Usage: python3 mergedir source_directory destination_directory')