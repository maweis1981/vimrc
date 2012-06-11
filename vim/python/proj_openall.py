"""Open all files in a project or dir, depending on where cursor is."""

from vim import *
from os.path import isdir, expanduser, join as pjoin
from os import sep
import time


def filelist():
    b = current.buffer
    l = current.line.strip()
    lnum = current.window.cursor[0]     # 1-based; buffer is 0-based
    filelst = []
    ldir = lproj = dirname = False

    # find out if cursor on dir name or project name
    if l and (l[0] in '~'+sep or l.endswith(sep)):
        if l[0] not in '~'+sep:
            # relative path
            l = pjoin(headpath, l)
        ldir = True
        dirname = l
    elif l.startswith("---"):
        lproj = True
    else:
        return []

    # loop over lines and add files
    while 1:
        try: l = b[lnum].strip()
        except: break
        lnum += 1

        if ldir and (l and l[0] in "~/"):
            break           # finished directory
        elif not l or l.strip().startswith('#'):
            continue        # blank lines & comments are allowed everywhere
        elif l[0] in "~/":
            dirname = l     # new directory
        elif l.startswith("---"):
            break           # finished project
        else:
            if dirname and l:
                if not isdir(expanduser(dirname)):
                    print "Error: missing directory (%s)" % dirname
                    time.sleep(1.5)
                    return []
                filelst.append(pjoin(dirname, l))   # add file

    return filelst

def openall():
    filelst = filelist()
    command(':call NextWin()')
    for fn in filelst:
        command(":e %s" % fn)

if __name__ == '__main__':
    openall()
