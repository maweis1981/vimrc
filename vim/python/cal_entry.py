"""Go to or create a new entry."""

from vim import *
from time import *
from datetime import *
import re


def search(pat, d=''):
    """Search for pattern. d='b' to search backwards, returns 0 if not found."""
    if d: d = ", '%s'" % d
    return int(eval("search('%s'%s)" % (pat, d)))

def getc():
    """Get char at cursor location."""
    return current.line[current.window.cursor[1]]

def entry():
    """Jump to or make new entry."""
    # find day number by tracing the bounding box.
    cur = current.window.cursor
    s = search('|', 'b')
    if not s: return

    command("normal 2lk")
    for x in range(20):
        if getc() == '-':
            break
        command("normal k")

    if getc() != '-':
        current.window.cursor = cur
        return
    command("normal j")
    if getc() == '[': command("normal 2l")

    day = eval("expand('<cWORD>')").rstrip(']')
    new = True

    if day.endswith('*'):
        new = False
        day = day[:-1]

    if not re.match("^\d{1,2}$", day):
        current.window.cursor = cur
        return

    if new: command("normal geelr*")    # add star - cmd: ge  e  l  r*

    # find what month we're at
    search("====== ", 'b')
    l = current.line.strip("= ")
    t = strptime(l, "%B %Y")
    target_d = date(t[0], t[1], int(day)).timetuple()

    # find needed day's entry or the last one before it if making new
    search("====== " + l)
    for x in range(int(day), 1, -1):
        d = date(t[0], t[1], x).timetuple()
        s = search("=== " + strftime("%a %B %d, %Y", d))
        if s: break

    # add new entry
    if new:
        # format e.g.: === Fri June 11, 2010
        lnum = current.window.cursor[0]
        b = current.buffer
        b[lnum:lnum] = ['', "=== " + strftime("%a %B %d, %Y", target_d)]
        current.window.cursor = (lnum+3, 0)
    else:
        command("normal j")


if __name__ == '__main__':
    entry()
