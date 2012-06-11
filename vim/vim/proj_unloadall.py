"""Unload (:bdelete) all files in a project or dir, depending on where cursor is.

pause to read messages: command("call input('Hit Enter')")
"""

from vim import *
import sys
from os.path import expanduser
sys.path.append(expanduser("~/.vim/python/"))
import proj_openall


def cur_fname():
    b = current.buffer
    name = current.line.strip()
    lnum = current.window.cursor[0]
    while 1:
        if not lnum: return
        lnum -= 1
        l = b[lnum].strip()
        if l[0] in "~/":
            return l


def unload_all():
    filelst = proj_openall.filelist()
    if not filelst:
        l = current.line.strip()
        if l and not l.startswith('#'):
            filelst = [l]

    if not filelst: return

    # make list of all listed buffers
    bnames = [b.name for b in buffers if b.name and not b.name.endswith(".proj")]
    tmp = [x.split('/')[-1] for x in bnames]

    bnums = []
    for bn in bnames:
        try: bnums.append(eval("bufnr('%s')" % bn))
        except: continue
    bnums = [b for b in bnums if int(eval("buflisted(%s)" % b)) > 0]
    project_buf = eval("bufnr('%')")
    command("call NextWin()")
    currb = eval("bufnr('%')")

    # make list of buf numbers we need to unload
    flbnums = []
    for bn in filelst:
        try: flbnums.append(eval("bufnr('%s')" % bn))
        except: continue

    flbnums = [n for n in flbnums if n != '-1']

    # if current buffer needs to be unloaded, we need to switch to some other buffer
    # to preserve windows layout
    switch_to = None
    for bn in bnums:
        if bn not in flbnums:
            switch_to = bn
            break

    # unload buffers
    for fn in filelst:
        try: bnr = eval("bufnr('%s')" % expanduser(fn))
        except: continue
        if int(eval("buflisted(%s)" % bnr)):
            command(":b %s" % bnr)
            if not int(eval("&modified")):
                if switch_to: command(":b %s" % switch_to)
                else: command("bnext")

                try:
                    command("bdelete %s" % bnr)
                except:
                    pass
            else:
                print "'%s' has unsaved changes" % fn

    # try to switch to original buffer; go back to project window
    if currb not in flbnums:
        command(":b %s" % currb)
    for x in range(10):
        command("call NextWin()")
        if eval("bufnr('%')") == project_buf:
            break


if __name__ == '__main__':
    unload_all()
