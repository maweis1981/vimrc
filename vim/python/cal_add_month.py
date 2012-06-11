"""Add new month to the calender."""

from vim import *
from calendar import *
from time import *
from re import sub
from datetime import date, timedelta

width = int(eval("g:py_cal_width"))


def mkmonth(t):
    """Make and return a list of lines for given month. `t` is a timetuple object."""
    wd = width - 2
    lst = monthcalendar(t[0], t[1])
    out = ["====== " + strftime("%B %Y", t)]    # e.g. June 2010

    # make line template
    daywidth = int(round(wd / 7)) - 2

    linetpl = ("%%-%ds| " % daywidth)*7
    linetpl = linetpl.rstrip()
    divtpl = ("%%-%ds|-" % daywidth)*6 + "%%-%ds|" % daywidth

    # add header
    header = "Mo Tu We Th Fr Sa Su".split()
    header = ' '*3 + linetpl % tuple(header)
    wd = len(header) - 1
    out.extend([header.replace('|', ' ').rstrip(), ' ' + '-'*wd])

    # add weeks
    for n, week in enumerate(lst):
        w = linetpl % tuple(week)
        # monthcalendar() returns 0s for non-existing days; replace with spaces
        out.append(" | " + sub("^0  | 0 |  0$", ' '*3, w))
        l = " | " + linetpl % tuple(' '*7)
        ll = " |-" + divtpl % tuple( ['-'*daywidth]*7 )
        if n+1 == len(lst):
            ll = ' ' + '-'*wd
        out.extend([l, ll])    # blank lines for notes

    out.append('')

    return out


def search(pat, d=''):
    """Search for pattern. d='b' to search backwards, returns 0 if not found."""
    if d: d = ", '%s'" % d
    return int(eval("search('%s'%s)" % (pat, d)))


def add_month():
    """Add next month."""
    b = current.buffer
    init, lnum = False, 0

    # make timetuple of next (or initial) month
    if len(b) == 1:
        # init empty file
        ttup = localtime()
        init = True
    else:
        command("normal gg")
        search("======-")
        lnum = current.window.cursor[0] - 1
        search("====== ", 'b')
        l = current.line.strip("= ")
        t = strptime(l, "%B %Y")
        d = date(t[0], t[1], t[2]) + timedelta(31)
        ttup = d.timetuple()

    out = mkmonth(ttup)
    if init:
        # 2-line separater of month views and day entries
        sepline = '='*(width-1) + '-'
        out.extend([sepline, sepline])

    # out.extend(['', ''])
    b[lnum:lnum] = out

    b.append(out[0])
    b.append('')

    command("set nolist")
    command("normal %dggzz" % (lnum+1))


if __name__ == '__main__':
    add_month()

