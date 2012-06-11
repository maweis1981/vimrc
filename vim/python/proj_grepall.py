"""Grep all files in a project or dir, depending on where cursor is."""

from vim import *
from string import join
from os.path import expanduser
import sys
sys.path.append(expanduser("~/.vim/python/"))
import proj_openall

def grepall():
    filelst = proj_openall.filelist()
    command(":call NextWin()")
    pat = eval("input('pattern: ')")
    if pat:
        try: command(":vimgrep %s %s" % (pat, join(filelst)))
        except error: pass  # print "Not Found"

if __name__ == '__main__':
    grepall()
