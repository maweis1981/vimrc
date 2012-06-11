"""Initialize fin file."""
from vim import *
from time import asctime
from string import join
import re

def fin_init():
    # get headers and initial line
    b = current.buffer
    lst = []
    for l in b:
        if l.strip():
            lst.append(l)
        if len(lst) == 2:
            break

    headers = re.split("\s\s+", lst[0])
    ncols = len(headers)
    maxlen = [len(h)+4 for h in headers]
    headers += ["date", "desc"]

    initline = re.split("\s\s+", lst[1])

    # make line template
    fldtpl = ''
    for x in maxlen:
        fldtpl += "%%-%ds" % x
    fldtpl += "%-13s%s"

    # make list of header, divider and rest of lines
    div = '-'*78
    t = asctime().split()[:3]
    initline += [join(t), 'initial']
    del b[:]
    b[0:0] = [fldtpl % tuple(headers), div] + [fldtpl % tuple(initline), '', div]
    command("let s:fin_fldtpl='%s'" % fldtpl)

if __name__ == '__main__':
    fin_init()
