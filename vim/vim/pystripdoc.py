"""Create a copy of buffer with stripped python comments and docstring."""
import re
from vim import *


def pystripdoc():
    # close preview window; copy the buffer into a new window
    command("pclose!")
    command("setlocal ft=python")
    command("silent %y a")
    command("below new")
    command("silent put a")

    cur = 0
    b = current.buffer
    end = len(b)
    startdel = comment = False
    dellst = []

    # make a list of lines to delete
    for cur in range(end):
        if cur >= len(b):
            break
        l = b[cur].strip()
        lst, lend = l.startswith, l.endswith
        if comment and not lst("#"):
            # end multiline comment
            dellst.append((startdel, cur))
            startdel = comment = False
            continue

        if startdel != False and lend('"""'):
            # end multiline docstring
            dellst.append((startdel, cur+1))
            startdel = False
            continue

        if lst('"""') and not re.match('^""".*"""$', l) and startdel == False:
            # start multiline docstring
            startdel = cur+1

        if not comment and lst("#"):
            # start multiline comment
            comment = True
            startdel = cur+1

        # single line dosctrings
        if startdel == False:
            if lst('"') and lend('"') and not lend('"""'):
                # dbl quote docstring
                dellst.append((cur+1,))
            if (lst("'") and lend("'")) or (lst('"""') and lend('"""') and l != '"""'):
                # single quote or triple quote docstring
                dellst.append((cur+1,))

    # delete lines
    dellst.reverse()
    for tup in dellst:
        if len(tup) == 1: command("%sd" % tup[0])
        else: command("%s,%sd" % tup)

    command("setlocal ft=python")
    command("setlocal previewwindow")


if __name__ == "__main__":
    pystripdoc()
