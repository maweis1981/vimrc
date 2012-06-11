"""
Align equal signs or comments in code.

Search for lines ahead and back from current line, processing all contiguous lines that
have align character. If `char` is not given, try to guess based on current line,
preferring '#'.
"""
import re
from vim import *

def exists(var):
    return int(eval("exists('%s')" % var))

def aligncode():
    # set up variables
    char = False
    if exists("a:1"): char = eval("a:1")    # arg from vim function
    lnum = orignum = current.window.cursor[0]
    b, l = current.buffer, current.line

    # figure out align char
    if char:
        alchar = ' %s ' % char
    else:
        if ' # ' in l: alchar = ' # '
        elif ' = ' in l: alchar = ' = '
        else: return
    lnums = []
    maxl = 0

    # search ahead and back for lines to process
    for step in (1, -1):
        while 1:
            try: l = b[lnum]
            except: break
            if alchar in l:
                lnums.append(lnum)
                tmp = len( l.split(alchar, 1)[0].rstrip() )
                if tmp > maxl: maxl = tmp
            else:
                break
            lnum += step
        lnum = orignum - 1

    if alchar == ' # ': maxl += 4   # give more padding to comments

    for lnum in lnums:
        l = b[lnum].split(alchar, 1)
        tpl = "%%-%ds%%s%%s" % maxl
        b[lnum] = tpl % (l[0].rstrip(), alchar, l[1].lstrip())


if __name__ == "__main__":
    aligncode()
