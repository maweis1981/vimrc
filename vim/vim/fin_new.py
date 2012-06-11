"""Add new entry."""

from vim import *
from string import join
from time import asctime
import re


def finnew():
    # find end of entries to insert new one
    b = current.buffer
    headers = re.split("\s\s+", b[0])
    ncols = len(headers) - 2

    # try get line template from fin_update()
    fldtpl = "%-10s"*(ncols) + "%-15s%s"
    if int(eval("exists('s:fin_fldtpl')")):
        fldtpl = eval("s:fin_fldtpl")

    command("normal G$")
    command("call search('-----', 'b')")
    lnum = current.window.cursor[0]
    while 1:
        lnum -= 1
        if b[lnum].strip():
            current.window.cursor = (lnum, 0)
            break

    # insert blank entry
    t = asctime().split()[:3]
    cols = [0] * ncols + [join(t), ' ']
    lnum -= 1
    b[lnum:lnum] = [fldtpl % tuple(cols)]

if __name__ == '__main__':
    finnew()
